<template>
  <vue-cal
    :events="events"
    :on-event-click="handleClick"
    :on-event-drag-create="handleDragCreate"
    :on-event-drop="handleDrop"
    style="height: 700px"
    time="24"
    locale="fa"
  />
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import VueCal from 'vue-cal'
import 'vue-cal/dist/vuecal.css'

const events = ref([])

const fetchEvents = async () => {
  try {
    const res = await axios.get('http://localhost:8000/api/events/')
    events.value = res.data.map(ev => ({
      ...ev,
      start: new Date(ev.start),
      end: new Date(ev.end),
    }))
  } catch (err) {
    console.error('خطا در دریافت رویدادها', err)
  }
}

onMounted(fetchEvents)

const handleClick = ({ event }) => {
  alert(`رویداد انتخاب شد:\n${event.title}`)
}

const handleDragCreate = async ({ start, end }) => {
  const title = prompt('عنوان تسک؟')
  if (!title) return

  try {
    await axios.post('http://localhost:8000/api/events/', {
      title,
      content: 'ایجاد شده از طریق تقویم',
      start: start.toISOString(),
      end: end.toISOString(),
    })
    fetchEvents()
  } catch (e) {
    alert('خطا در ذخیره تسک جدید')
  }
}

const handleDrop = async ({ event }) => {
  try {
    await axios.put(`http://localhost:8000/api/events/${event.id}/`, {
      ...event,
      start: event.start.toISOString(),
      end: event.end.toISOString(),
    })
  } catch (e) {
    alert('خطا در ذخیره تغییر زمان')
  }
}
</script>

