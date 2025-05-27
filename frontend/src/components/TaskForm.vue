<script setup>
import { ref } from 'vue'
import axios from 'axios'

const title = ref('')
const content = ref('')
const error = ref('')
const result = ref(null)
const loading = ref(false)

async function analyzeTask() {
  error.value = ''
  result.value = null

  if (!content.value.trim()) {
    error.value = 'توضیح تسک (content) الزامی است.'
    return
  }

  loading.value = true

  try {
    const res = await axios.post('http://localhost:8000/api/parse-time/', {
      title: title.value,
      content: content.value,
    })

    result.value = res.data
  } catch (e) {
    error.value = e.response?.data?.error || 'خطا در پردازش زمان'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <form @submit.prevent="analyzeTask" class="space-y-4">
    <input
      v-model="title"
      type="text"
      placeholder="عنوان تسک (مثلاً: جلسه تیم)"
      class="border border-gray-300 rounded px-4 py-2 w-full"
    />
    <input
      v-model="content"
      type="text"
      placeholder="توضیح تسک (مثلاً: فردا ساعت ۹ صبح)"
      class="border border-gray-300 rounded px-4 py-2 w-full"
    />
    <button
      :disabled="loading"
      type="submit"
      class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
    >
      {{ loading ? 'در حال تحلیل...' : 'تحلیل تسک' }}
    </button>
    <p v-if="error" class="text-red-600 text-sm">{{ error }}</p>

    <div v-if="result" class="mt-4 border p-4 rounded bg-gray-50">
      <p><strong>عنوان:</strong> {{ result.title }}</p>
      <p><strong>شروع:</strong> {{ result.start }}</p>
      <p><strong>پایان:</strong> {{ result.end }}</p>
    </div>
  </form>
</template>
