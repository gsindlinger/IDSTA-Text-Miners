<script>
    import { fade } from 'svelte/transition';

    export let active;
    let imageCounter = 0;
    let isLoaded = false;
    const images = [
        {
            path: "src/lib/images/pipeline/1.png",
            description: "As a first step, we identified a list of the most relevant artists of German rap of the past years." +
            " To do this, we used the Spotify API to search for playlists created by Spotify itself and named 'Deutschrap xxxx', "+ 
            "whereby xxxx stands for any year from the period 1998-2022. All the artists there were entered in a list.",
            posX: 0,
            posY: 0,
            width: "270px",
        },
        {
            path: "src/lib/images/pipeline/2.png",
            description: "Subsequently, the previously created list of artists was used to download their artist ID and most relevant songs via the lyrics plattform Genius." +
            " Meta-information like date, album, etc. were added. Around 10,000 songs could be scraped with this.",
            posX: "0px",
            posY: "50px",
            width: "317px"
        },
        {
            path: "src/lib/images/pipeline/3.png",
            description: "Since the raw data of the lyrics are rather unstructered, several steps had to be taken to clean them up." +
            " Many songs are not or only partially written in German and had to be ignored accordingly. "+
            "The remaining lyrics were finally pre-treated by means of tokenisation, stopword removal,"+
            " lemmatisation and the manual deletion of filling words such as 'ey', 'oh' etc.",
            posX: "300px",
            posY: "115px",
            width: "195px"
        },
        {
            path: "src/lib/images/pipeline/4.png",
            description: "As a first approach, we examined the raw quantity of different words of certain categories of discrimination, racism and hate." +
            " For each category, we developed a vocabulary of similar terms using the Word2Vec framework and then counted the occurrences of words in"+
            " these categories within the lyrics.",
            posX: "500px",
            posY: "30px",
            width: "190px"
        },
        {
            path: "src/lib/images/pipeline/5.png",
            description: "Subsequently, the previously created list of artists was used to download their artist ID and most relevant songs via the lyrics service." +
            " Meta-information like date, album, etc. were added.",
            posX: "500px",
            posY: "105px",
            width: "190px"
        },
        {
            path: "src/lib/images/pipeline/6.png",
            description: "Subsequently, the previously created list of artists was used to download their artist ID and most relevant songs via the lyrics service." +
            " Meta-information like date, album, etc. were added.",
            posX: "500px",
            posY: "155px",
            width: "190px"
        },
        {
            path: "src/lib/images/pipeline/7.png",
            description: "Subsequently, the previously created list of artists was used to download their artist ID and most relevant songs via the lyrics service." +
            " Meta-information like date, album, etc. were added.",
            posX: "695px",
            posY: "50px",
            width: "150px"
        },
    ]
    
    $: if(active) {
        setTimeout(() => isLoaded = true, 500);
    }


    const handleClickNext = function() {
        imageCounter = (imageCounter + 1) % images.length
    }

    const handleClickPrevious = function() {
        imageCounter = (imageCounter + images.length - 1) % images.length
    }

</script>


<div class="page-content-motivation background-image-motivation">
    <div class="content-wrapper">
            {#if active || isLoaded}
            <div class="header-wrapper" in:fade={{delay: 300, duration: 500}}>
                <div class="citation">
                    <p class="header-font">building a natural language processing pipeline</p>
                </div>
            </div>
            {/if}
            {#if isLoaded}
            <div class="text-wrapper" in:fade={{delay: 150, duration: 500}}>
                <div class="topic-wrapper">
                    <button class="next-icon" on:click={handleClickPrevious}>
                        <i class="fa-solid fa-angle-left"></i>
                    </button>
                    <div class="pipeline-wrapper">
                        <div class="multiple-images">
                        {#each images as image, i}
                            {#if i <= imageCounter}
                                <img transition:fade src={image.path} alt={image.description} style="top: {image.posY}; left: {image.posX}; width: {image.width};">
                            {/if}
                        {/each}
                        </div>
                        <div class="image-text">
                            <p>{images[imageCounter].description}</p>
                        </div>
                    </div>
                    <button class="next-icon" on:click={handleClickNext}>
                        <i class="fa-solid fa-angle-right"></i>
                    </button>
                </div>
                <div class="progress-line">
                    {#each images as _, i}
                    <div class="hline" class:hline-active="{i <= imageCounter}" style="left: {14*i}%"></div>
                    {/each}
                </div>
            </div>
            {/if}
    </div>
</div>

<style>

    .image-text {
        height: 8rem;
        padding-top: 0.5rem;
    }

    .progress-line{
        width: 95%;
        margin: 1rem;
        position: relative;
    }

    .hline {
        position: absolute;
        margin: 1%;
        width: 13%;
        height: 4px;
        @apply bg-slate-600;
    }

    .hline-active {
        background-color: var(--color-text);
    }

    .topic-wrapper {
        display: flex;
        width: 100%;
        height: 100%;
    }
    .next-icon {
        height: 100%;
        display: flex;
        align-items: center;
        font-size: 2rem;
        border: 0;
        background: transparent;
        cursor: pointer;

    }
    .multiple-images {
        width: 845px;
        height: 260px;
        position: relative;
        padding: 0 1rem;
        margin-left: 1rem;
    }

    .pipeline-wrapper {
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .text-wrapper {
        height: 100%;
        flex-direction: column;
    }

    .text-wrapper p {
        padding: 0 0.5rem;
    }

    .multiple-images img {
        position: absolute;
    }

    
    .citation-wrapper{
        width: 100%;
        display: flex;
        justify-content: flex-end;
    }
    
    .citation {
        width: 100%;
        padding: 2rem;
    }
    
    
    .background-image-motivation {
        background-image: linear-gradient(to bottom, rgb(5, 9, 54), rgba(245, 246, 252, 0.3), rgb(5, 9, 54)), 
        url('../images/background-images/1.jpg');
    }
    
    </style>