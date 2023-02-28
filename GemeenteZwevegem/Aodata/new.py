string = "create table if not exist test(id varchar(255), creationDate varchar(255), modificationDate varchar(255), status integer, entryTypeId varchar(255), typeId varchar(255), categoryId varchar(255), subcategoryId varchar(255), branchId varchar(255), operatorGroupId varchar(255), operatorId varchar(255), processingStatusId varchar(255), callDate varchar(255), targetDate varchar(255), completed boolean, completionDate varchar(255), responded boolean, closed boolean, closureDate varchar(255), escalated boolean, deescalated boolean, "
size = len(string)
string = string[:- 2]
print(string)