<template>
  <div>
    <el-container style="min-height: 100vh">
      <el-header
        style="
          display: flex;
          align-items: center;
          border-bottom: 1px solid #ddd;
          background-color: #fff;
        "
      >
        <!-- 左侧标题区域 -->
        <div
          style="flex: 1; display: flex; align-items: center; font-size: 24px; font-weight: bold"
        >
          <img style="width: 40px" src="@/assets/imgs/logo.png" alt="" />
          <div style="margin-left: 5px">智能实验室预约系统</div>
        </div>

        <!-- 右侧管理员下拉菜单（这就是你缺少的部分） -->
        <div style="display: flex; align-items: center">
          <el-dropdown>
            <!-- 触发下拉的头部内容 -->
            <div style="display: flex; align-items: center; cursor: pointer">
              <img v-if="userInfo?.avatar" :src="userInfo.avatar" alt="" style="width: 30px; border-radius: 50%" />
              <div style="margin-left: 3px">{{ userInfo?.name || userInfo?.username }}</div>
            </div>
            <!-- 下拉菜单项 -->
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click="goPerson">个人信息</el-dropdown-item>
                <el-dropdown-item @click="handleLogout">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>

      <el-container>
        <el-aside width="220px">
          <el-menu router style="height: 100%" default-active="/manager/home">
            <el-menu-item index="/manager/home">
              <el-icon><icon-menu /></el-icon>
              <span>系统首页</span>
            </el-menu-item>
            <el-menu-item index="/manager/lab">
              <el-icon><House /></el-icon>
              <span>实验室管理</span>
            </el-menu-item>
            <el-menu-item index="/manager/equ">
              <el-icon><Setting /></el-icon>
              <span>设备列表管理</span>
            </el-menu-item>
            <el-menu-item index="/manager/user">
              <el-icon><User /></el-icon>
              <span>用户管理</span>
            </el-menu-item>
          </el-menu>
        </el-aside>

        <el-main>
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import { logout } from '@/utils/auth'
import { Menu as IconMenu, House, Setting, User } from '@element-plus/icons-vue'
import { useRouter } from 'vue-router' // 1. 需要引入 useRouter
import { useUser } from '@/utils/user'

const router = useRouter() // 2. 定义 router

const { userInfo } = useUser()

const goPerson = () => {
  router.push('/manager/profile')
}

const handleLogout = () => {
  logout() // 3. 函数需要加括号调用
  router.push('/login') // 4. route 改为 router
}
</script>
