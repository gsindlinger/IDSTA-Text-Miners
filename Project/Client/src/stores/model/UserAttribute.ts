export class UserAttribute {
    private userId: string
    private attributeValueId: string

    constructor(userId: string, attributeValueId: string) {
        this.userId = userId;
        this.attributeValueId = attributeValueId;
    }
}
