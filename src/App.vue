<template>
  <div id="app" class="flex flex-col items-center">
    <h1 class="text-4xl font-bold text-gray-800 mb-4">List of Words</h1>
    <ul class="w-full md:w-3/4 lg:w-1/2 xl:w-1/3 mb-4">
      <li class="p-4 bg-white rounded-lg shadow-md" v-for="word in words" :key="word.word">
        <h3 class="text-2xl font-bold text-gray-800">{{ word.word }}</h3>
        <p class="text-lg font-semibold text-gray-700 mb-2">Translation: {{ word.translation }}</p>
        <p>Example: {{ word.example }}</p>
        <p>Example (English): {{ word.example_en }}</p>
        <p>Emoji: {{ word.emoji }}</p>
        <p>Tags: {{ word.tags }}</p>
        <p>Difficulty: {{ word.difficulty }}</p>
        <p>Part of speech: {{ word.part_of_speech }}</p>
        <p>Gender: {{ word.gender }}</p>
        <p>Plural: {{ word.plural }}</p>
        <p>Synonyms: {{ word.synonyms }}</p>
        <p>Antonyms: {{ word.antonyms }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import words from '@/french.json'

export default {
  data() {
    return {
      words: words
    }
  }
}
</script>

<style>
/* Add your CSS here */
</style>
