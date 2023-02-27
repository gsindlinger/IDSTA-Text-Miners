// @ts-nocheck

import {get, writable} from "svelte/store";
import { SearchApi } from "../api/SearchApi";

export const displaySong = writable({})
export const searchSongs = writable([])
export const isMounted = writable(false)
export const searchIsActive = writable(false);
export const couldFindSearchResults = writable(false);
export const occurrences = writable('')


export const loadInitialData = async function() {
    await SearchApi.getRandomSong()
		.then((response) => {
			displaySong.set(response.results)
			isMounted.set(true)
		})
		.catch(() => alert('Error fetching search results!'));
    
    await SearchApi.getOccurrences()
        .then((response) => {
            occurrences.set(response.results)
            console.log(get(occurrences))
        })
        .catch(() => alert('Error fetching occurrences data!'))
}

export const fetchSearchResults = async function(text: string) {
    await SearchApi.searchSong(text)
		.then((response) => {
            if(response.length === 0) {
                couldFindSearchResults.set(false)
            }else{
                couldFindSearchResults.set(true)
                searchSongs.set(response.results.map(x => x[0]))
            }
		})
		.catch(() => alert('Error fetching search results!'))
}



// https://stackoverflow.com/questions/7128675/from-green-to-red-color-depend-on-percentage
export const percentColors = [
    { pct: 0.0, color: { r: 0xff, g: 0x00, b: 0 } },
    { pct: 0.5, color: { r: 0xff, g: 0xff, b: 0 } },
    { pct: 1.0, color: { r: 0x00, g: 0xff, b: 0 } } ];


// https://stackoverflow.com/questions/7128675/from-green-to-red-color-depend-on-percentage
export const getColorForPercentage = function(pct) {
    for (var i = 1; i < percentColors.length - 1; i++) {
        if (pct < percentColors[i].pct) {
            break;
        }
    }
    var lower = percentColors[i - 1];
    var upper = percentColors[i];
    var range = upper.pct - lower.pct;
    var rangePct = (pct - lower.pct) / range;
    var pctLower = 1 - rangePct;
    var pctUpper = rangePct;
    var color = {
        r: Math.floor(lower.color.r * pctLower + upper.color.r * pctUpper),
        g: Math.floor(lower.color.g * pctLower + upper.color.g * pctUpper),
        b: Math.floor(lower.color.b * pctLower + upper.color.b * pctUpper)
    };
    return 'rgb(' + [color.r, color.g, color.b].join(',') + ')';
    // or output as hex if preferred
};

export const getArtistName = function(song) {
    if(song.artist_name) {
        if(song.writer_artists.length > 1) {
            let tempArray = song.writer_artists.filter(x => x != song.artist_name)            
            return song.artist_name +
            " feat. " + 
            tempArray.join(', ')
        } else {
            return song.artist_name
        }
    } else if(song.writer_artists.length > 1) {
        return song.writer_artists[song.writer_artists.length-1] + 
            " feat. " + 
            song.writer_artists.slice(0, song.writer_artists.length-1).join(', ')
    }else if(song.writer_artists.length === 1) {
        return song.writer_artists[0]
    }else if(song.producer_artists.length > 0){
        return song.producer_artists[0]
    }else {
        return ""
    }
}


