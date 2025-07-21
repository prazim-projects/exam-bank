<script setup lang='ts'>

var count = ref(4)
function increment() {
	 count.value++; 
}

</script>

<template> 
    <div class=""> 
        <h1> home </h1>
        <h1>Selam Exam Archive</h1>
    <p></p>
    <form>
	<label> name </label>	<input>
    </form>
    </div>
    <div class="text-primary" >
    <button  class='bg-white rounded-4xl' @click="increment"> click me</button>
    </div>
    <h4> {{count}}</h4>

</template>
