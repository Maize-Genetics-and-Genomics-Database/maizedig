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