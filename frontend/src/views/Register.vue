<template>
  <div class="auth-page"><div class="auth-shell"><section class="auth-intro"><div class="auth-brand"><span class="brand-mark"><img src="@/assets/imgs/logo.png" alt="" /></span><span>LAB / SPACE<small>智能实验室预约系统</small></span></div><div class="auth-story"><span class="eyebrow">A SPACE FOR WHAT'S NEXT</span><h1>为每一次<br />探索<span>，</span><br />留出空间。</h1><p>从预约实验室到管理设备，让专注留给真正重要的事。</p></div><div class="auth-footer">LAB / SPACE <span>探索，从这里开始 ↗</span></div></section><section class="auth-form"><div class="auth-form-inner"><span class="section-index">GET STARTED / 02</span><h2>创建你的账号</h2><p>加入实验室，开启你的探索。</p><el-form ref="formRef" :rules="rules" :model="form" label-width="0px" style="width: 100%">
        <el-form-item prop="username">
          <el-input
            size="large"
            v-model="form.username"
            placeholder="请输入账号"
            :prefix-icon="User"
          />
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            type="password"
            size="large"
            v-model="form.password"
            placeholder="请输入密码"
            :prefix-icon="Lock"
            show-password
          />
        </el-form-item>
        <el-form-item prop="confirmPassword">
          <el-input
            type="password"
            size="large"
            v-model="form.confirmPassword"
            placeholder="请确认密码"
            :prefix-icon="Lock"
            show-password
          />
        </el-form-item>
        <div>
          <el-button
            size="large"
            type="primary"
            :loading="loadingValue"
            style="width: 100%"
            @click="register"
            >创建账号</el-button
          >
          <div style="text-align: right; margin-top: 20px">
            已有账号？请
            <router-link style="color: var(--el-color-primary)" to="/login">登录</router-link>
          </div>
        </div>
      </el-form></div></section></div></div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { User, Lock } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import { registerApi } from '@/api/auth'
import router from '@/router'

const form = reactive({
  username: '',
  password: '',
  confirmPassword: ''
})

const loadingValue = ref(false)

const formRef = ref()

const validatePass = (rule, value, callback) => {
  if (value === '') {
    callback(new Error('请确认密码'))
  } else {
    if (value !== form.password) {
      callback(new Error('两次密码输入不一致'))
    } else {
      callback()
    }
  }
}
const rules = {
  username: [{ required: true, message: '请输入账号', trigger: 'blur' }],
  password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
  confirmPassword: [{ validator: validatePass, trigger: 'blur' }]
}

const register = async () => {
  const valid = await formRef.value.validate().catch(() => false)
  if (!valid) return
  loadingValue.value = true
  try {
    const res = await registerApi(form)
    if (res.code === 200) {
      ElMessage.success('注册成功')
      await router.push('/login')
    }
  } finally {
    loadingValue.value = false
  }
}
</script>

<style scoped>
.auth-page {
  padding: 0;
}

.auth-shell {
  width: 100%;
  min-height: 100vh;
  border-radius: 0;
  box-shadow: none;
}
</style>
