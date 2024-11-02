<script>
// @ts-nocheck

	import {scaleLinear, max, line, curveNatural, color} from "d3";
	import { categories_mapping, occurrences, colorCategoryMapping } from "../../stores/GeneralStore";
	import { fade } from 'svelte/transition';


	export let categorySelection = []
	let points = []
	let colorArray = []
	$: points = getSelectedPoints(categorySelection)

	const getSelectedPoints = function(categorySelection) {
		let points_helper = []
		let colorArray_helper = []
		for(let i = 0; i < categorySelection.length; i++) {
			if(categorySelection[i].checked) {
				let names = $occurrences.map(x => x[0]).flat()

				let category_mapped_values = Object.values(categories_mapping)
				let category_index = category_mapped_values.findIndex(x => x === categorySelection[i].value)
				let categories_mapped_keys = Object.keys(categories_mapping)
				let finalIndex = names.findIndex(x => x === categories_mapped_keys[category_index] + "_normalized")

			
				let temp = $occurrences[finalIndex].slice(1, $occurrences[finalIndex].length-1).map(x => Number(x))
				points_helper.push(temp)
				colorArray_helper.push(colorCategoryMapping[i])
			}
		}
		colorArray = colorArray_helper
		return points_helper
	}
	
	let years_unfiltered = $occurrences[0].slice(1).map(x => Number(x))
	let years = $occurrences[0].slice(1).filter((x, index) => index % 2 == 0).map(x => Number(x))

	const lineGenHelper = function(line) {
		return years_unfiltered.map((item, index) => ({
			category: item,
			value: line[index]}))
	}
	
	
	const calcYTicks = function(points) {
        let step = Math.max(...points.flat()) / 4
        let retArray = []
        for(let i = 0; i < 5; i++) {
            retArray.push(i*step)
        }
        return retArray
    }

    let yTicks = []
    $: yTicks = calcYTicks(points)

		
	$: width =  600;
	$: height = 1000;
	$: margin = { top: 40, right: 40, bottom: 40, left: 50 }
		 
	// const yMax = tweened(null, { duration });   
	// const xMax = tweened(null, { duration });
	
	// $: yMax.set(max(lineData, d => d.total));
	// $: xMax.set(max(lineData, d => d.Year));
		
	$: xMax = 2022
	$: yMax = Math.max(...points.flat())
	
	$: xScale = scaleLinear()
	  .domain([1998, xMax])
	  .range([margin.left, width - margin.right])
	
	$: yScale = scaleLinear()
	  .domain([0, yMax])
	  .range([height - margin.top,margin.bottom])
	
	$: lineGen = line()
	  .x(d => xScale(d.category)+margin.left-margin.right)
	  .y(d => yScale(d.value))
		
	$: linePath = function(line) {
		return lineGen(lineGenHelper(line))
	} 
		
	</script>
	<div class="chart" bind:clientWidth={width} bind:clientHeight={height}>
		{#if points.length > 0}
		<svg tra:fade={{duration: 500}}>
				{#each points as l, index}
					<path class="line" style="stroke: {colorArray[index]}" d={linePath(l)}/>
				{/each}


			<!-- y axis -->
			<g class="axis y-axis" transform="translate(0,{margin.top})">
				{#each yTicks as tick}
					<g class="tick tick-{tick}" transform="translate(0, {yScale(tick) - margin.bottom})">
						<line x2="100%"></line> 
						<text y="-4">
							{(Math.round(tick * 100)/100).toFixed(2)}
							{#if tick === Math.max(...yTicks)}
								<tspan dx="5" class="y-axis-label">average occurrences per song</tspan>
							{/if}
						</text>
					</g>   
				{/each}   
			</g>

			<!-- x axis -->
			<g class="axis x-axis">
				{#each years as category}  
					<g class="tick" transform="translate({xScale(category)+margin.left-margin.right},{height})">   
						<text x="0" y="{-8}">{category}</text>
					</g> 
				{/each} 
			</g>

		</svg>
		{/if}

	</div>
	
	<style>

		.y-axis-label{
			font-style: italic;
			font-size: 0.8rem;
		}

		.line {
		transition: all 1s;
			fill: none;
			stroke-width: 4;
			stroke: black;
		}


		svg {
			padding: 0;
			border-radius: 0.75rem;
			overflow: visible;
			position: relative;
			width: 100%;
		}

		polyline {
			fill: none;
			stroke-linejoin: round;
			stroke-linecap: round;
			stroke-width: 1.5px;
			stroke: #fffa;
		}

		path {
			stroke: none;
		}
		pre {
			display: inline-block;
			background: white;
			padding: 0.5rem;
			border-radius: 5px;
			white-space: nowrap;
			overflow: hidden;
			text-overflow: ellipsis;
			max-width: 100%;
			margin: 5px 0 0 0;
		}

		.chart {
			width: 100%;
			height: 100%;
			margin: 0 auto;
		}

		.tick {
			font-family: var(--font-body);
			font-size: 1rem;
			font-weight: 200;
		}

		.tick line {
			@apply stroke-slate-600;
			stroke-dasharray: 2;
		}

		.tick text {
			fill: #ccc; 
			text-anchor: start;
			@apply fill-slate-600;
		}

		.tick.tick-0 line {   
			stroke-dasharray: 0;
		} 

		.x-axis .tick text {   
			text-anchor: middle; 
		} 
	</style>
	
	