/**
 * Object that represents a grouping of image tags
 * @params group, imageKey, siteUrl
 * @return none
 *
 * Updated by Kyoung Tak Cho
 * Updated date: Jun 10 13:10:08 CDT 2019
 */
function TagGroup(group, imageKey, siteUrl) {
	//this.tags = {};
	this.tags = [];
	this.lastModified = TaggableUtil.toDate(group.lastModified);
	this.dateCreated = TaggableUtil.toDate(group.dateCreated);
	this.name = group.name;
	this.key = group.id;
	if (group.hasOwnProperty('tags')) {
		for (var i = 0; i < group.tags.length; i++) {
			var tag = group.tags[i];
			var colorArr = tag.color;
			var tagPoints = tag.points;
			var description = tag.name;
			var geneLinks = tag.geneLinks;
			var id = tag.id;
			var userName = tag.user;
			//this.tags[id] = new Tag(id, userName, colorArr, tagPoints, description, geneLinks, imageKey, siteUrl, this);
			this.tags.push(new Tag(id, userName, colorArr, tagPoints, description, geneLinks, imageKey, siteUrl, this));
		}
	}
};

TagGroup.prototype.getName = function() {
	return this.name;
};

TagGroup.prototype.getDateCreated = function() {
	return this.dateCreated;
};

TagGroup.prototype.getLastModified = function() {
	return this.lastModified;
};

TagGroup.prototype.getId = function() {
	return this.key;
};

TagGroup.prototype.getTags = function() {
	return this.tags;
};

TagGroup.prototype.addTag = function(tag) {
	this.tags[tag.getId()] = tag;
};