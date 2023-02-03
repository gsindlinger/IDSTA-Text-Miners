export class AttributeValue {
    id?: string
    value: string
    attributeDefinitionId: string

    constructor(attributeDefinitionId: string, name: string, id?: string) {
        if(id) {
            this.id = id;
        }
        this.value = name;
        this.attributeDefinitionId = attributeDefinitionId;
    }
}


