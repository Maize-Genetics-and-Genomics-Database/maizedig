/**
 * GeneLink object
 * @params id, feature
 * @methods
 *   getId()
 *   getUniqueName()
 *   getName()
 *   getAllele()
 *   getOrganismId()
 * @fields
 *   id
 *   name
 *   allel
 *   uniqueName
 *   organismId
 *
 * Updated by Kyoung Tak Cho
 * Updated date: Nov 01 14:04:05 CDT 2017
 */
function GeneLink(id, feature) {
	this.id = id;
	this.name = feature.name;
    this.allele = feature.allele;
	this.uniqueName = feature.uniqueName;
	this.organismId = feature.organismId;
};

GeneLink.prototype.getId = function() {
	return this.id;
};

GeneLink.prototype.getUniqueName = function() {
	return this.uniqueName;
};

GeneLink.prototype.getName = function() {
    return this.name;
};

GeneLink.prototype.getAllele = function() {
	return this.allele;
};

GeneLink.prototype.getOrganismId = function() {
	return this.organismId;
};