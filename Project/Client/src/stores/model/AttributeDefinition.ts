export class AttributeDefinition {
    id?: string
    name: string

    constructor(name: string, id?: string) {
        if(id) {
            this.id = id;
        }
        this.name = name;
    }
}

