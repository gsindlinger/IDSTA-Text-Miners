import Api from "./Api";
import { occurrencesStr, random, search } from "./ApiStrings";

export class SearchApi{
    static getRandomSong = async () : Promise<any> => {
        const response = await Api.get(random);
        return response;
    };

    static searchSong = async (body: string) : Promise<any> => {
        const response = await Api.post(search,
            JSON.stringify({text: body}));
        return response;
    };

    static getOccurrences = async () : Promise<any> => {
        const response = await Api.get(occurrencesStr);
        return response;
    };
    
}