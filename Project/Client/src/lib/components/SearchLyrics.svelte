<script>
// @ts-nocheck

	import { displaySong, fetchSearchResults, getArtistName, searchIsActive, searchSongs } from "../../stores/GeneralStore";
	import { fade } from 'svelte/transition';
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher();
    const closeSearch = function() {
        searchSongs.set([])
        searchText = ""
        searchTextChecker = false;
        dispatch('closeSearch')
    }

    const selectSong = function(song) {
        displaySong.set(song)
        setTimeout(() => searchIsActive.set(false), 100)
        searchSongs.set([])
        searchText = ""
        searchTextChecker = false;
    }

    let searchText = ""
    let timeout

    const keyPressed = function() {
        if (timeout) clearTimeout(timeout);
        timeout = setTimeout(async () => {
            await fetchSearchResults(searchText);
            searchText.length > 0 ? searchTextChecker = true : searchTextChecker = false;
        }, 300);
    }

    let searchTextChecker = false;
    

</script>

{#if $searchIsActive}
    <div class="search-page-overall" transition:fade>
        <div class="search-page-bottom">
            <div class="search-results">
                {#if $searchSongs.length > 0}
                    {#each $searchSongs.slice(0,5) as song}
                        <button class="song-short-info reset-button" on:click={selectSong(song)}>
                            <div class="song-title">{song.title}</div>
                            <div class="song-artist">{getArtistName(song)}</div>
                        </button>
                    {/each}
                {:else if searchTextChecker}
                    <div class="backup">No songs could be found based on your search.</div>
                {/if}
            </div>
            <div class="search-page-bottom-data">
                <p>Enter the name of a song or artist...</p>
                <input bind:value={searchText} on:keydown={()=> keyPressed()} type="text" class="searchBar">
                <button class="close-button reset-button" on:click={closeSearch}>
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>
        </div>
    </div>
{/if}

<style>

    .backup {
        padding: 3rem;
        font-size: 1.2rem;
    }

    .song-short-info {
        @apply bg-gray-400;
        width: 30rem;
        padding: 0.5rem 0.2rem;
        margin: 1rem;
        border-radius: 1rem;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    .song-short-info:hover {
        box-shadow: 0 0 1rem rgba(33,33,33,.5);
    }

    .song-title {
        font-size: 1.3rem;
        color: white;
        padding-left: 2rem;
    }

    .song-artist {
        font-style: italic;
        color: white;
        padding-left: 2rem;
    }



    .search-results {
        background-color: #4152f1;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }


    .close-button {
        position: absolute;
        top: 2rem;
        right: 5rem;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        font-size: 2rem;
        @apply text-gray-400;
    }

    .search-page-overall {
        width: 100vw;
        height: 100vh;
        top: 0;
        left: 0;
        position: fixed;
        background-color: hsla(0,0%,100%,.75);
        z-index: 1000;
    }

    .search-page-bottom {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: absolute;
        background-color: rgb(5, 9, 54);
        bottom: 0;
        left: 0;
        width: 100%;
        @apply text-gray-400;
    }

    .search-page-bottom-data {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 15rem;
        position: relative;
    }

    .search-page-bottom p {
        padding: 1.5rem;
        font-size: 1.2rem;
    }

    .searchBar {
        background-color: #fff;
        border: none;
        border-radius: 1rem;
        display: block;
        font-size: 1.1rem;
        font-family: var(--font-body);
        margin: 0 auto;
        max-width: 30rem;
        padding: 1em 2em;
        width: 100%;
        color: rgb(5, 9, 54);
        padding-bottom: 1rem;
    }

    .searchBar:focus {
        border: none;
    }
    

</style>