<script>
	import { scaleLinear, scaleBand } from 'd3-scale';
    import { slide } from 'svelte/transition';

	export let points = [
		{ x_value: 'love', y_value: 5, color: "red" },
	];  

    $: x_values = points.map(d => d.x_value)
    $: y_values = points.map(d => d.y_value)
    $: y_values, getYTicks()

    let yTicks = []
	export let yticks = [];



    const getYTicks = function() {
		if(Math.max(...y_values) >= 5) {
			let step = Math.ceil(Math.max(...y_values) / 5)
			yTicks = []
			for(let i = 1; i <= 5; i++) {
				yTicks.push(step*i)
			}
		}else if(Math.max(...y_values) >= 1) {
			yTicks = []
			for(let i = 1; i <=Math.max(...y_values)+1; i++) {
				yTicks.push(i)
			}
		}else{
			yTicks = []
			let step = Math.ceil(Math.max(...y_values)*1.05/5 * 100) / 100 
			for(let i = 1; i <= 5; i++) {
				yTicks.push((step*i).toFixed(2))
			}
		}
    }
	
	export let xTicks = [1990, 1995, 2000, 2005, 2010, 2015];
	const padding = { top: 30, right: 15, bottom: 40, left: 30 };

	export let width = 500;
	export let height = 200; 

    
	$: xScale = scaleBand()
		.domain(x_values)
		.range([padding.left-10, width - padding.right+5])
	  .padding(0.2);

	$: yScale = scaleLinear()
		.domain([0, Math.max.apply(null, yTicks)])
		.range([height - padding.bottom, padding.top]); 

	$: innerWidth = width - (padding.left + padding.right);
	$: barWidth = innerWidth / xTicks.length;
</script>

<style>

	h2 {
		text-align: center;
	}

	.chart {
		width: 100%;
		max-width: 500px;
		margin: 0 auto;
	}

	svg {
		position: relative;
		width: 100%;
		height: 200px;
	}

	.tick {
		font-family: var(--font-body);
		font-size: .725em;
		font-weight: 200;
	}

	.tick line {
		stroke: #e2e2e2;
		stroke-dasharray: 2;
	}

	.tick text {
		fill: #ccc; 
		text-anchor: start;
	}
 
	.tick.tick-0 line {   
		stroke-dasharray: 0;
	} 
 
	.x-axis .tick text {   
		text-anchor: middle; 
	} 

	.bars rect {
   	transition: all 1s;
		stroke: none;   
		opacity: 0.8;
	}
</style> 
 
<div class="chart" bind:clientWidth={width} bind:clientHeight={height}>
	<svg>
		<!-- y axis -->
		<g class="axis y-axis" transform="translate(0,{padding.top})">
			{#each yTicks as tick}
				<g class="tick tick-{tick}" transform="translate(0, {yScale(tick) - padding.bottom})">
					<line x2="100%"></line> 
					<text y="-4">{tick}</text>
				</g>   
			{/each}   
		</g>  

		<!-- x axis -->    
		<g class="axis x-axis">
			{#each points as point (point.x_value)}  
				<g class="tick" transform="translate({xScale(point.x_value)},{height})">   
					<text x="{barWidth/2}" y="{point.index % 2 != 0 || Object.keys(points).length < 3 ? '-8' : '-30'}">{point.x_value}</text>
				</g> 
			{/each} 
		</g> 
 
		<g class='bars'> 
			{#each points as point (point.x_value)}  
				<rect
					x="{xScale(point.x_value)}"
					y="{yScale(point.y_value)-8}" 
					width="{barWidth - 4}" 
					height="{height - padding.bottom - yScale(point.y_value)}"
                    fill="{point.color}"
					in:slide="{{duration: 1000}}"
				></rect> 
			{/each}
		</g>
	</svg>
</div>
