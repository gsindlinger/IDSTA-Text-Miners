<script>
    import { fade } from 'svelte/transition';
    import logo1 from "$lib/images/pipeline/1.png";
    import logo2 from "$lib/images/pipeline/2.png";
    import logo3 from "$lib/images/pipeline/3.png";
    import logo4 from "$lib/images/pipeline/4.png";
    import logo5 from "$lib/images/pipeline/5.png";
    import logo6 from "$lib/images/pipeline/6.png";
    import logo7 from "$lib/images/pipeline/7.png";



    export let active;
    let imageCounter = 0;
    let isLoaded = false;
    const images = [
        {
            path: logo1,
            description: "As a first step, we identified a list of the most relevant artists of German rap of the past years." +
            " To do this, we used the Spotify API to search for playlists created by Spotify itself and named 'Deutschrap xxxx', "+ 
            "whereby xxxx stands for any year from the period 1998-2022. All the artists there were entered in a list.",
            posX: 0,
            posY: 0,
            width: "270px",
        },
        {
            path: logo2,
            description: "Subsequently, the previously created list of artists was used to download their artist ID and most relevant songs via the lyrics plattform Genius." +
            " Meta-information like date, album, etc. were added. Around 10,000 songs could be scraped with this.",
            posX: "0px",
            posY: "50px",
            width: "317px"
        },
        {
            path: logo3,
            description: "Since the raw data of the lyrics are rather unstructered, several steps had to be taken to clean them up." +
            " Many songs are not or only partially written in German and had to be ignored accordingly. "+
            "The remaining lyrics were finally pre-treated by means of tokenisation, stopword removal,"+
            " lemmatisation and the manual deletion of filling words such as 'ey', 'oh' etc."+
            " Furthermore, since the used models require full sentences, we had to split the lyrics in meaningful sentences: For that we used an auto-punctuation model that can receive raw non-punctuated text and put commas and dots where needed.",
            posX: "300px",
            posY: "115px",
            width: "195px"
        },
        {
            path: logo4,
            description: "As a first approach, we examined the raw quantity of different words of certain categories of discrimination, racism and hate." +
            " For each category, we developed a vocabulary of similar terms using the Word2Vec framework on a pretrained model on german text data." +
            " Afterwards, we manually checked this vocabulary by removing some terms and adding others." +
            " Finally, we counted the occurrences of words in these categories within the lyrics." +
            " Insights into that analysis you'll find on the last page in the area word occurrences.",
            posX: "500px",
            posY: "30px",
            width: "190px"
        },
        {
            path: logo5,
            description: "In addition, we looked for different pretrained models for sentiment analysis that we could apply to the lyrics."+
            " We were able to find the german-sentiment-bert and toxicity-v2 models available on the huggingface platform. "+
            "For both models, we analysed each line independently and calculated a mean value across the entire song. "+
            "The sentiment analysis takes values in the range of -100% to 100%, where -100% represents a strongly negative song and 100% represents a more positive song. "+
            "The toxicity classifier takes values for the two classes neutral and toxic values from 0% to 100% each.",
            posX: "500px",
            posY: "105px",
            width: "190px"
        },
        {
            path: logo6,
            description: "In order to fit the sentiment of the songs to our labels of interest, we've chosen to use a zero-shot classifier model that can classify a piece of text into custom labels." +
            " We've used the following labels: neutral, lovely, violent, racist, homophobic, misogynistic, friendly, positive and sad. " +
            "These custom labels are more labels than we initially wanted to classify, but this allows the model to have other choices if the text doesn't necessarily fitting to one of our labels of interest. ", 
            posX: "500px",
            posY: "155px",
            width: "190px"
        },
        {
            path: logo7,
            description: "All the results of the analyses were then collected and evaluated. The results are presented here on this website. Details on the results and the procedure can be found in the associated report.",
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
        padding: 0 0 0 1rem;
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