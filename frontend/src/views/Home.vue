<template>
  <div class="dashboard">
    <section class="welcome-panel">
      <div class="welcome-copy"><div class="eyebrow"><span></span> YOUR LAB WORKSPACE</div><h1>你好，{{ userInfo?.name || '同学' }}<span>。</span></h1><p>每一个好想法，都值得一个好空间。<br />在这里找到实验室，安排你的下一次探索。</p><el-button class="welcome-action" @click="$router.push('/manager/ai-chat')">与 AI 助手对话 <span>↗</span></el-button></div>
      <div class="welcome-art" aria-hidden="true"><div class="orbit orbit-one"></div><div class="orbit orbit-two"></div><div class="orbit-center">LAB<span>SPACE</span></div><span class="art-cross cross-one">+</span><span class="art-cross cross-two">+</span><span class="art-caption">IDEAS IN MOTION<br />01 — 03</span></div>
    </section>
    <div class="section-heading"><div><span class="section-index">01 / OVERVIEW</span><h2>空间概览</h2></div><span>你的实验室工作台</span></div>
    <div class="stat-grid"><div class="stat-card" v-for="(item, index) in statCards" :key="item.label"><span class="stat-number">0{{ index + 1 }}</span><div class="stat-label">{{ item.label }}</div><div class="stat-value">{{ item.value }}<small>{{ item.unit }}</small></div><div class="stat-line"></div></div></div>
    <div class="section-heading shortcut-heading"><div><span class="section-index">02 / QUICK ACCESS</span><h2>从这里开始</h2></div><span>常用功能，一步直达</span></div>
    <div class="shortcut-grid"><button class="shortcut" v-for="(item, index) in shortcuts" :key="item.path" @click="$router.push(item.path)"><span class="shortcut-index">0{{ index + 1 }}</span><span class="shortcut-content"><strong>{{ item.label }}</strong><small>{{ item.desc }}</small></span><span class="shortcut-arrow">↗</span></button></div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useUser } from '@/utils/user'
import { getLabPageList } from '@/api/lab'
import { getReservationPageList } from '@/api/reservation'

const { userInfo } = useUser()

const labTotal = ref('-')
const reservationTotal = ref('-')

const statCards = computed(() => [
  { label: '开放实验室', value: labTotal.value, unit: '间' },
  { label: '相关预约', value: reservationTotal.value, unit: '条' },
  { label: '智能助手', value: '在线', unit: '' }
])


const shortcuts = computed(() => {
  const list = [{ label: 'AI 智能助手', desc: '提问、查询与预约', path: '/manager/ai-chat' }]
  if (userInfo.value?.role !== 'admin') list.push(
    { label: '实验室列表', desc: '浏览开放空间与设备', path: '/manager/lablist' },
    { label: '我的预约', desc: '查看预约进度', path: '/manager/my-reservation' }
  )
  if (userInfo.value?.role === 'admin') {
    list.push(
      { label: '预约审核', desc: '处理预约申请', path: '/manager/audit-reservation' },
      { label: '实验室管理', desc: '维护实验室信息', path: '/manager/lab' },
      { label: '设备管理', desc: '管理实验室设备', path: '/manager/equipment' },
      { label: '用户管理', desc: '查看与维护用户', path: '/manager/user' }
    )
  }
  return list
})

onMounted(async () => {
  try {
    const labRes = await getLabPageList({ page: 1, page_size: 1, status: 1 })
    if (labRes.code === 200) labTotal.value = labRes.data?.total ?? 0
  } catch {
    labTotal.value = '-'
  }
  try {
    const resRes = await getReservationPageList({ page: 1, page_size: 1 })
    if (resRes.code === 200) reservationTotal.value = resRes.data?.total ?? 0
  } catch {
    reservationTotal.value = '-'
  }
})
</script>
