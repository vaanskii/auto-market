<template>
  <div class="w-full">
    <button 
    class="block px-6 py-2 rounded md:hover:bg-black uppercase w-full"
            v-for="sLocale in supportedLocales"
            :key="`locale-${sLocale}`"
            @click="switchLanguage(sLocale)"
            >
      {{ t(`locale.${sLocale}`) }}
    </button>
  </div>
</template>

<script>
import { useI18n } from 'vue-i18n'
import { useRouter } from 'vue-router'
import Tr from '@/i18n/translation'

export default {
  setup() {
    const { t, locale } = useI18n()
    const supportedLocales = Tr.supportedLocales

    const router = useRouter()

    const switchLanguage = async (newLocale) => {
      await Tr.switchLanguage(newLocale)

      try {
        await router.replace({ params: { locale: newLocale } })
      } catch (e) {
        console.error(e)
        router.push('/')
      }
    }

    return { t, locale, supportedLocales, switchLanguage }
  }
}
</script>