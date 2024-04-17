<template>
  <h1 class="uppercase text-5xl font-bold mb-10 pt-40 text-center">{{ $t('blogs.header') }}</h1>
  <div class="flex justify-center flex-col items-center py-8">
    <!-- Blog Posts -->
    <div
      v-for="blog in blogs"
      :key="blog.id"
      class="flex flex-col justify-center items-center bg-[#E6E6E6] w-[80%] shadow-4xl rounded-xl py-8 mb-14 reveal-item"
    >
      <img :src="blog.image" alt="" class="max-w-full lg:max-w-md rounded-lg">
      <div class="p-6 rounded-lg mt-4">
        <h2 class="text-2xl font-semibold text-center">{{ $t(blog.question) }}</h2>
        <p class="mt-4 text-gray-700">{{ $t(blog.answer) }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router'
import Trans from '@/i18n/translation'

export default {
  setup() {
    const blogs = [
      {
        id: 1,
        image: '/mechanic.png',
        question: 'blogs.question1',
        answer: 'blogs.answer1'
      },
      {
        id: 2,
        image: '/mechanic.png',
        question: 'blogs.question2',
        answer: 'blogs.answer2'
      },
      {
        id: 3,
        image: '/mechanic.png',
        question: 'blogs.question3',
        answer: 'blogs.answer3'
      },
      {
        id: 4,
        image: '/mechanic.png',
        question: 'blogs.question4',
        answer: 'blogs.answer4'
      }
    ];

    return {
      Trans,
      blogs
    }
  },
}
</script>
