import Api from "./Api";
import { random, search } from "./ApiStrings";

export class SearchApi{
    static getRandomSong = async () : Promise<any> => {
        const response = await Api.get(random);
        return response;
    };

    static searchSong = async (body: string) : Promise<any> => {
        const response = await Api.get(search);
        return response;
    };
    
}