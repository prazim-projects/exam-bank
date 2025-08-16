<script setup lang='ts'>


</script>

<template> 
    <div class="flex flex-row w-full p-2 text-black"> 
        <div class="p-2">
            <h1> home </h1>
            <h1>Selam Exam Archive</h1>
            <p></p>
        </div>
        <div class="m-2">
            <form >
	            <label> name </label>	<input class="bg-gray-100">
            </form>
            <button  class=' bg-purple-600 rounded-4xl p-3 m-5' @click="increment"> click me</button>
            <h4> {{count}}</h4>
        </div >
        <div class="p-2 flex flex-row"> <content />     <examUpload /></div>
    </div>
   
</template>
