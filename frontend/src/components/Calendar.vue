<template>
  <vue-cal
    :events="events"
    @event-create="createEvent"
    style="height: 700px"
  />
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import 'vue-cal/dist/vuecal.css'
import VueCal from 'vue-cal'

const events = ref([])

onMounted(async () => {
  try {
    const res = await axios.get('http://localhost:8000/api/events/')
    events.value = res.data
  } catch (err) {
    console.error('خطا در دریافت رویدادها', err)
  }
})

const createEvent = async (event) => {
  try {
    const res = await axios.post('http://localhost:8000/api/events/', {
      title: event.title || 'رویداد جدید',
      start: event.start,
      end: event.end,
      all_day: event.allDay || false,
      description: event.content || '',
    })
    events.value.push(res.data)
  } catch (err) {
    console.error('خطا در ایجاد رویداد', err)
  }
}
</script>
