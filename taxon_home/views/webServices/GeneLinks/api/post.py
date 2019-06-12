"""
    PostAPI for GeneLink
    @methods
      createGeneLink()
        return metadata
    @fields
      fields
      user

    Updated by Kyoung Tak Cho
    Last Updated: Nov 2 10:11:44 CDT 2017
"""
import taxon_home.views.util.ErrorConstants as Errors
from taxon_home.models import Tag, GeneLink, Feature, Variation
from django.core.exceptions import ObjectDoesNotExist
from renderEngine.WebServiceObject import WebServiceObject, LimitDict
from django.db import transaction, DatabaseError
from django.http import HttpResponse, HttpResponseNotFound

class PostAPI:
    
    def __init__(self, user, fields=None):
        self.user = user
        self.fields = fields
        
    '''
        Creates a new tag with the given parameters
        
        @param points: The points for a tag in an array of dictionaries
            format: [{"x" : 256, "y" : 350}, ...]
        @param description: The description for this tag
        @param color: The color array for this tag
            format: [r, g, b]
    '''
    @transaction.commit_on_success 
    def createGeneLink(self, tagKey, name=None,  allele=None, organismId=None, isKey=True):
        metadata = WebServiceObject()

        try:
            if isKey:
                tag = Tag.objects.get(pk__exact=tagKey)
            else:
                tag = tagKey
        except (ObjectDoesNotExist, ValueError):
            raise Errors.INVALID_TAG_GROUP_KEY
        
        if not tag.writePermissions(self.user):
            raise Errors.AUTHENTICATION

        try:
            feature = None
            if name and organismId:
                feature = Feature.objects.filter(name=name, organism=organismId)

            if not feature:
                error = "Could not find a feature with the parameters: "
                if name and organismId:
                    error += "name: " + name + ", organismId: " + organismId

                raise Errors.NO_MATCHING_FEATURE.setCustom(error)
            elif len(feature) > 1:
                error = "Multiple matches for parameters: "
                if name and organismId:
                    error += "name: " + name + ", organismId: " + organismId

                error += "\n\n Responses: \n\n"
                
                for f in feature:
                    error += "uniquename: " + f.uniquename + ", name: " + f.name + ", organism: " + f.organism.common_name + "\n\n"
                
                raise Errors.NO_MATCHING_FEATURE.setCustom(error)

            if allele:
                vID = None

                vID = Variation.objects.using('mgdb').filter(name__exact=allele)
                if not vID:
                    errorAllele = Errors.NO_MATCHING_ALLELE.setCustom(allele)
                    raise errorAllele

            geneLink = GeneLink(tag=tag, feature=feature[0], user=self.user, allele=allele)
            geneLink.save()
        except DatabaseError as e:
            transaction.rollback()
            raise Errors.INTEGRITY_ERROR.setCustom(str(e))
        
        # limit metadata return
        metadata.limitFields(self.fields)
            
        metadata.put('id', geneLink.pk)
        metadata.put('user', geneLink.user.username)
        metadata.put('tagId', geneLink.tag.pk)
        metadata.put('feature',
            LimitDict(self.fields, {
                'uniqueName' : geneLink.feature.uniquename,
                'name' : geneLink.feature.name,
                'allele': geneLink.allele,
                'organismId' : geneLink.feature.organism.organism_id
            })
        )
        
        return metadata
        
        
