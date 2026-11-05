<template>
  <div class="workspace">
    <aside class="sidebar">
      <router-link class="brand" to="/manager/home">
        <span class="brand-mark"><img src="@/assets/imgs/logo.png" alt="" /></span>
        <span><strong>LAB / SPACE</strong><small>智能实验室预约系统</small></span>
      </router-link>
      <div class="nav-label">WORKSPACE <span>工作空间</span></div>
      <el-menu router :default-active="route.path" class="workspace-menu">
        <el-menu-item index="/manager/home"><el-icon><IconMenu /></el-icon><span>工作台</span></el-menu-item>
        <el-menu-item v-if="userInfo?.role === 'student'" index="/manager/lablist"><el-icon><OfficeBuilding /></el-icon><span>实验室列表</span></el-menu-item>
        <el-menu-item v-if="userInfo?.role === 'admin'" index="/manager/lab"><el-icon><House /></el-icon><span>实验室管理</span></el-menu-item>
        <el-menu-item v-if="userInfo?.role === 'admin'" index="/manager/equipment"><el-icon><Setting /></el-icon><span>设备管理</span></el-menu-item>
        <el-menu-item v-if="userInfo?.role === 'admin'" index="/manager/user"><el-icon><User /></el-icon><span>用户管理</span></el-menu-item>
        <el-menu-item v-if="userInfo?.role === 'student'" index="/manager/my-reservation"><el-icon><Tickets /></el-icon><span>我的预约</span></el-menu-item>
        <el-menu-item v-if="userInfo?.role === 'admin'" index="/manager/audit-reservation"><el-icon><DocumentChecked /></el-icon><span>预约审核</span></el-menu-item>
        <el-menu-item index="/manager/ai-chat"><el-icon><ChatDotRound /></el-icon><span>AI 智能助手</span></el-menu-item>
      </el-menu>
      <div class="sidebar-note"><span class="note-dot"></span><div>让研究更专注<small>从一次有序的预约开始</small></div></div>
    </aside>
    <div class="workspace-body">
      <header class="topbar">
        <div><span class="topbar-kicker">LAB MANAGEMENT / {{ userInfo?.role === 'admin' ? 'ADMIN' : 'MEMBER' }}</span><div class="topbar-title">{{ pageTitle }}</div></div>
        <el-dropdown @command="handleCommand" trigger="click">
          <button class="account-trigger" type="button" aria-label="账户菜单">
            <img v-if="userInfo?.avatar" :src="userInfo.avatar" alt="" />
            <span v-else class="account-avatar">{{ (userInfo?.name || userInfo?.username || 'U').slice(0, 1) }}</span>
            <span class="account-name"><strong>{{ userInfo?.name || userInfo?.username || '用户' }}</strong><small>{{ userInfo?.role === 'admin' ? '管理员' : '学生' }}</small></span>
            <el-icon><ArrowDown /></el-icon>
          </button>
          <template #dropdown><el-dropdown-menu><el-dropdown-item command="profile">个人信息</el-dropdown-item><el-dropdown-item command="password">修改密码</el-dropdown-item><el-dropdown-item divided command="logout">退出登录</el-dropdown-item></el-dropdown-menu></template>
        </el-dropdown>
      </header>
      <main class="workspace-main"><router-view /></main>
    </div>
  </div>
</template>

<script setup>
import { logout } from '@/utils/auth'
import {
  Menu as IconMenu,
  House,
  Setting,
  User,
  OfficeBuilding,
  Tickets,
  DocumentChecked,
  ChatDotRound,
  ArrowDown
} from '@element-plus/icons-vue'
import { useRouter, useRoute } from 'vue-router'
import { computed } from 'vue'
import { useUser } from '@/utils/user'

const router = useRouter()
const route = useRoute()
const pageTitle = computed(() => ({
  '/manager/home': '工作台', '/manager/lablist': '实验室列表', '/manager/lab': '实验室管理',
  '/manager/equipment': '设备管理', '/manager/user': '用户管理', '/manager/my-reservation': '我的预约',
  '/manager/audit-reservation': '预约审核', '/manager/ai-chat': 'AI 智能助手',
  '/manager/profile': '个人信息', '/manager/password': '修改密码', '/manager/lab-equipment': '实验室设备'
})[route.path] || '工作台')

const { userInfo } = useUser()

const handleCommand = (command) => {
  if (command === `profile`) {
    router.push(`/manager/profile`)
  } else if (command === `password`) {
    router.push(`/manager/password`)
  } else if (command === `logout`) {
    logout()
    router.push('/login')
  }
}
</script>
