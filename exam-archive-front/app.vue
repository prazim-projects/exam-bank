<script setup lang='js'>

var count = ref(4)
function increment() {
	 count.value++; 
}

</script>

<template>
  <div>
    <NuxtRouteAnnouncer />
    <h1>Hello Exam Archive</h1>
    <p>blaatfool</p>
    <form>
	<label> name </label>	<input>
    </form>
    <button @click="increment"> click me</button>
    <h4> {{count}}</h4>

    </div>
</template>
