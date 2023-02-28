<script lang="ts">
// @ts-nocheck

    
    import { fade } from 'svelte/transition';
    import { displaySong, getColorForPercentage, isMounted, loadInitialData, searchIsActive, getArtistName, categories_mapping } from '../../stores/GeneralStore';
    import { onMount } from "svelte";
    import BarChart from '$lib/components/BarChart.svelte';
    import SearchLyrics from '$lib/components/SearchLyrics.svelte';



    export let active;
    let isLoaded = false;

    $: if(active && $isMounted) {
        setTimeout(() => isLoaded = true, 1000);
    }


    onMount(async () => {
        await loadInitialData()
    })

    const replaceBracketsInLyrics = function(str: string) {
        str = str
        .replace("(\n", "(")
        .replace("\n)", ")")
        .replace("[\n", "[")
        .replace("\n]","]")
        return str
    }

    const getSentimentColor = function(value: float) {
        let percentage = (value + 1) / 2
        return getColorForPercentage(percentage)
    }

    const getMapperValue = function(lst, value) {
        if(value < -0.5) {
            return lst[0]
        }else if(value < 0) {
            return lst[1]
        }else if(value < 0.5) {
            return lst[2]
        }else{
            return lst[3]
        }
    }


    const toxicity_mapper = ['neutral', 'neutral', 'toxic', 'toxic', ]
    const sentiment_mapper = ['negative', 'slightly negative', 'slightly positive', 'positive']

    const colors1 = ["#040936", "#0F21C7", "#4152F1", "#8691EC"]


    const class_score_mapping = {
        "frauenfeindlich": "misogynistic",
        "freundlich": "friendly",
        "gewalttätig": "violent",
        "homophob": "homophobic",
        "liebevoll": "affectionate",
        "neutral": "neutral",
        "positiv": "positive",
        "rassistisch": "racist",
        "traurig": "sad"
    }

    const getTop4Occurences = function(song) {
        if(song.matched_categories) {
            console.log("items_bla")
            console.log(song)
            var items = Object.keys(song.matched_categories).map(function(key) {
                return [key, song.matched_categories[key]];
            });
            items.sort(function(first, second) {
                return second[1] - first[1];
            });
            const result = items.slice(0,4).map((x, index) => {
                return {
                    x_value: categories_mapping[x[0]],
                    y_value: x[1],
                    color: colors1[index],
                    index: index
                }
            })
            return result
        }
        return ""
    }

    const getYTicksOccurences = function(song) {
        if(song.matched_categories) {
            let y_values = getTop4Occurences(song).map(d => d.y_value)
            let yTicks = []
            if(Math.max(...y_values) >= 5) {
                let step = Math.ceil(Math.max(...y_values) / 5)
                for(let i = 1; i <= 5; i++) {
                    yTicks.push(step*i)
                }
            }else{
                for(let i = 1; i <=Math.max(...y_values)+1; i++) {
                    yTicks.push(i)
                }
            }
            return yTicks
        }else{
            return ""
        }
    }

    const getTop3Classes = function(song) {
        if(song.total_class_score) {
            var items = Object.keys(song.total_class_score).map(function(key) {
                return [key, song.total_class_score[key]];
            });
            items.sort(function(first, second) {
                return second[1] - first[1];
            });
            const result = items.slice(0,4).map((x, index) => {
                return {
                    x_value: class_score_mapping[x[0]],
                    y_value: x[1],
                    color: colors1[index],
                    index: index
                }
            })
            return result
        }else{
            return ""
        }
    }

    </script>
    
    <div class="page-content-motivation background-image-motivation">
        <div class="content-wrapper content-wrapper-lyrics">
            {#if (active || isLoaded) && $isMounted}
                <div class="header-wrapper header-wrapper-lyrics">
                    <div class="header-without-search">
                        <div class="header-lyrics">
                            <div class="artist-image">
                                <img src="{$displaySong.primary_artist_picture}" alt="{$displaySong.writer_artists[$displaySong.writer_artists.length-1]}">
                            </div>
                            <div class="citation">
                                <h3 class="header-font">{$displaySong.title}</h3>
                                {#if getArtistName($displaySong) != ""}
                                <h4 class="subtitle-song">
                                    {getArtistName($displaySong)}
                                </h4>
                                {/if}
                            </div>
                        </div>
                    </div>
                    <div class="header-search">
                        <button class="search-item-text-wrapper reset-button" on:click={() => searchIsActive.set(true)}>
                            <i class="fa-solid fa-magnifying-glass"></i>
                            <div class="text-left">Search for song / artist</div>
                        </button>
                    </div>
                </div>
                <div class="text-wrapper" in:fade="{{ duration: 1000 }}">
                    <p>{replaceBracketsInLyrics($displaySong.lyrics.trim())}</p>    
                </div>
                <div class="sentiment-wrapper analysis-box" style="color: {getSentimentColor($displaySong.sentiment_value)}">
                    <h3>Sentiment</h3>
                    <div 
                        class="analysis-donut"
                        style="border-color: {getSentimentColor($displaySong.sentiment_value)}"
                    >
                        {Math.round($displaySong.sentiment_value * 100) + "%"}
                    </div>
                    <div class="sentiment-interpretation">{getMapperValue(sentiment_mapper, $displaySong.sentiment_value)}</div>
                </div>
                <div class="toxicity-wrapper analysis-box" style="color: {getSentimentColor($displaySong.toxicity_value*(-1))}">
                    <h3>Toxicity</h3>
                    <div class="analysis-donut"
                    style="border-color: {getSentimentColor($displaySong.toxicity_value)}"
                    >
                    {Math.round(Math.abs($displaySong.toxicity_value * 100)) + "%"}</div>
                    <div class="sentiment-interpretation">{getMapperValue(toxicity_mapper, $displaySong.toxicity_value)}</div>
                </div>
                <div class="zero-shot-wrapper analysis-box">
                    <h3>Classification</h3>
                    <BarChart points={getTop3Classes($displaySong)} yticks={getYTicksOccurences($displaySong)}/>
                </div>
                <div class="occurrences-wrapper analysis-box">
                    <h3>Word occurrences</h3>
                    {#if Object.keys($displaySong.matched_categories).length > 0}
                        <BarChart points={getTop4Occurences($displaySong)} yticks={getYTicksOccurences($displaySong)}/>
                    {:else}
                        <div class="occurrences-fallback">
                            <p>No occurences of categories count.</p>
                        </div>
                    {/if}
                </div>
            {/if}
        </div>
        <SearchLyrics on:closeSearch={() => searchIsActive.set(false)}/>
    </div>
    
    <style>

    .search-item-text-wrapper{
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        @apply text-gray-400;
    }

    .search-item-text-wrapper div {
        width: 7rem;
        padding-left: 0.5rem;
    }

    .header-search {
        @apply text-gray-400;
        display: flex;
        align-items: center;
        padding-right: 2rem;
    }


    .header-search i {
        font-size: 2rem;
    }

    .occurrences-fallback {
        display: flex;
        justify-content: center;
        width: 100%;
        height: 100%;
        text-align: center;
        padding-top: 3rem;
        @apply text-gray-300;
    }

    .analysis-box {
        display: flex;
        flex-direction: column;
        padding: 0 1rem;
        justify-content: center;
        align-items: center;
    }

    .analysis-box h3 {
        @apply text-gray-200;
        font-family: var(--font-nixie);
        font-size: 1.2rem;
        text-decoration: underline;
        padding-bottom: 0.5rem;
        text-align: center;
    }

    .analysis-donut {
        width: 5rem;
        height: 5rem;
        font-size: 1.2rem;
        border-radius: 50%;
        border: 1.2rem solid;
        border-color: black;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 0.5rem;
    }


    .content-wrapper {
        display: grid;
        grid-template-columns: 18% 64% 18%;
        grid-template-rows: auto 1fr 1fr;
    }

    .header-wrapper-lyrics {
        grid-column-start: 1;
        grid-column-end: 4;
        grid-row-start: 1;
        grid-row-end: 2;
        justify-content: flex-start;
        padding-bottom: 2rem;
        display: flex;
        justify-content: space-between;
    }

    .text-wrapper {
        overflow-y: auto;
        margin-bottom: 2rem;
        position: relative;
        display: flex;
        grid-column-start: 2;
        grid-column-end: 3;
        grid-row-start: 2;
        grid-row-end: 4;
        flex-grow: 1;
    }

    .occurrences-wrapper {
        grid-column-start: 1;
        grid-column-end: 2;
        grid-row-start: 2;
        grid-row-end: 3;
    }

    .sentiment-wrapper {
        grid-column-start: 3;
        grid-column-end: 4;
        grid-row-start: 2;
        grid-row-end: 3;
    }

    .toxicity-wrapper {
        grid-column-start: 3;
        grid-column-end: 4;
        grid-row-start: 3;
        grid-row-end: 4;
    }

    .zero-shot-wrapper {
        grid-column-start: 1;
        grid-column-end: 2;
        grid-row-start: 3;
        grid-row-end: 4;
    }

    .artist-image {
        width: 12rem;
        height: 12rem;
    }

    .artist-image img {
        object-fit: cover;
        height: inherit;
        width: inherit;
        object-position: top;
    }

    .header-lyrics {
        display: flex;
    }

    .text-wrapper p {
        position: absolute;
        top: 0;
        width: auto;
        white-space: pre-line;
        text-align: left;
    }
    
    .subtitle-song {
        padding-left: 1rem;
        font-size: 1.5rem;
        font-family: var(--font-nixie);
        @apply text-gray-400;

    }

    
    .citation {
        width: 100%;
        padding: 2rem;
    }
    
    
    .background-image-motivation {
        background-image: linear-gradient(to bottom, rgb(5, 9, 54), rgba(245, 246, 252, 0.2), rgb(5, 9, 54)), 
        url('../images/background-images/7.jpg');
    }
    
    
    </style>