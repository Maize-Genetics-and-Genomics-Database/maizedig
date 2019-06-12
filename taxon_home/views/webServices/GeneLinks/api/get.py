"""
    GetAPI for GeneLink
    @methods
      getGeneLink()
        return metadata
    @fields
      fields
      user

    Updated by Kyoung Tak Cho
    Last Updated: Nov 1 14:01:35 CDT 2017
"""
import taxon_home.views.util.ErrorConstants as Errors
from taxon_home.models import GeneLink
from django.core.exceptions import ObjectDoesNotExist
from renderEngine.WebServiceObject import WebServiceObject, LimitDict

class GetAPI:
    
    def __init__(self, user=None, fields=None):
        self.user = user
        self.fields = fields
    
    '''
        Gets all the tags in the database that are private
    '''
    def getGeneLink(self, geneLinkKey, isKey=True):
        metadata = WebServiceObject()
        
        try:            
            if isKey:
                geneLink = GeneLink.objects.get(pk__exact=geneLinkKey)
            else:
                geneLink = geneLinkKey
        except (ObjectDoesNotExist, ValueError):
            raise Errors.INVALID_GENE_LINK_KEY
        except Exception:
            raise Errors.INTERNAL_ERROR
        
        if not geneLink.readPermissions(self.user):
            raise Errors.AUTHENTICATION
        
        metadata.limitFields(self.fields)
            
        metadata.put('id', geneLink.pk)
        metadata.put('user', geneLink.user.username)
        metadata.put('tagId', geneLink.tag.pk)
        metadata.put('feature',
            LimitDict(self.fields, {
                'uniqueName' : geneLink.feature.uniquename,
                'name': geneLink.feature.name,
                'allele': geneLink.allele,
                'organismId' : geneLink.feature.organism.organism_id
            })
        )
        return metadata
