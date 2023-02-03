<script>
	import { fade } from "svelte/transition";
</script>

<div in:fade="{{ duration: 1500 }}" class="container">
    <div class="chevron"></div>
    <div class="chevron"></div>
    <div class="chevron"></div>
  </div>

<style lang="scss">
$base: 0.6rem;

.container {
 position: fixed;
 bottom: 0;
 right: 0;
 margin: 10rem 7rem;
}

.chevron {
  position: absolute;
  width: $base * 3.5;
  height: $base * 0.8;
  opacity: 0;
  transform: scale(0.3);
  animation: move-chevron 3s ease-out infinite;
}

.chevron:first-child {
  animation: move-chevron 3s ease-out 1s infinite;
}

.chevron:nth-child(2) {
  animation: move-chevron 3s ease-out 2s infinite;
}

.chevron:before,
.chevron:after {
 content: '';
 position: absolute;
 height: 100%;
 width: 50%;
 @apply bg-gray-400;
}

.chevron:before {
 left: 0;
 transform: skewY(30deg);
}

.chevron:after {
 right: 0;
 width: 50%;
 transform: skewY(-30deg);
}

@keyframes move-chevron {
 25% {
  opacity: 1;
	}
 33.3% {
  opacity: 1;
  transform: translateY($base * 3.8);
 }
 66.6% {
  opacity: 1;
  transform: translateY($base * 5.2);
 }
 100% {
  opacity: 0;
  transform: translateY($base * 8) scale(0.5);
 }
}
</style>