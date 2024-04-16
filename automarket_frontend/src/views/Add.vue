<template>
    <div class="md:pt-40 pt-14">
        <h1 class="text-center mb-10">add car</h1>
        <form action="#" class="flex md:flex-col flex-col space-y-5">
            <!-- Main specifications -->
            <div class="flex items-center justify-center">
                <div class="p-4 md:mt-0 mt-20 w-[800px]">
                    <div class="flex bg-[#E6E6E6] rounded-md shadow-4xl md:flex-row ">
                        <div class="p-5 w-full">
                            <h3 class="my-4 text-2xl font-semibold text-gray-700 uppercase text-center">main specifications</h3>
                            <div class="grid md:grid-cols-3 gird-cols-1 gap-4">
                                <div class="flex flex-col space-y-1">
                                    <label for="manufacturer" class="text-sm font-semibold text-gray-500">Manufacturer</label>
                                    <select id="manufacturer" class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                    </select>
                                </div>

                                <div class="flex flex-col space-y-1">
                                    <label for="model" class="text-sm font-semibold text-gray-500">Model</label>
                                    <select id="model" class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                    </select>
                                </div>

                                <div class="flex flex-col space-y-1">
                                    <label for="category" class="text-sm font-semibold text-gray-500">Category</label>
                                    <select id="category" class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                    </select>
                                </div>

                                <div class="flex flex-col space-y-1">
                                    <label for="type" class="text-sm font-semibold text-gray-500">Type</label>
                                    <select id="type" class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                        <option value="">FOR SELL</option>
                                        <option value="">FOR RENT</option>
                                    </select>
                                </div>

                                <div class="flex flex-col space-y-1">
                                    <label for="year" class="text-sm font-semibold text-gray-500">Year</label>
                                    <input placeholder="Enter year" type="number" id="year" class="placeholder-gray-500 border border-gray-300  cursor-pointer text-black bg-white px-4 rounded py-2 outline-none" />
                                </div>
                                <div class="flex flex-col space-y-1">
                                    <label for="price" class="text-sm font-semibold text-gray-500">Price</label>
                                    <input placeholder="Enter year" type="number" id="price" class="placeholder-gray-500 border border-gray-300  cursor-pointer text-black bg-white px-4 rounded py-2 outline-none" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Primary features -->
            <div class="flex items-center justify-center">
                <div class="p-4 md:mt-0 mt-20 w-[800px]">
                    <div class="flex bg-[#E6E6E6] rounded-md shadow-4xl md:flex-row ">
                        <div class="p-5 w-full">
                            <h3 class="my-4 text-2xl font-semibold text-gray-700 uppercase text-center">primary features</h3>
                            <div class="grid md:grid-cols-2 gird-cols-1 gap-4">

                                <div class="flex flex-col space-y-1">
                                    <label for="location" class="text-sm font-semibold text-gray-500">Location</label>
                                    <select id="location" class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                    </select>
                                </div>

                                <div class="flex flex-col space-y-1">
                                    <label for="enginev" class="text-sm font-semibold text-gray-500">Engine volume</label>
                                    <input placeholder="Engine volume" type="number" id="enginev" class="placeholder-gray-500 border border-gray-300  cursor-pointer text-black bg-white px-4 rounded py-2 outline-none" />
                                </div>

                                <div class="flex flex-col space-y-1">
                                    <label for="milage" class="text-sm font-semibold text-gray-500">Milage km</label>
                                    <input placeholder="Enter milage" type="number" id="milage" class="placeholder-gray-500 border border-gray-300  cursor-pointer text-black bg-white px-4 rounded py-2 outline-none" />
                                </div>

                                <div class="flex flex-col space-y-1">
                                    <label for="fuel" class="text-sm font-semibold text-gray-500">Fuel type</label>
                                    <select id="fuel" class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                    </select>
                                </div>

                                <div class="flex flex-col space-y-1">
                                    <label for="transmission" class="text-sm font-semibold text-gray-500">Transmission</label>
                                    <select id="transmission" class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                    </select>
                                </div>

                                <div class="flex flex-col space-y-1">
                                    <label for="cylinders" class="text-sm font-semibold text-gray-500">Cylinders</label>
                                    <select id="cylinders" class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                    </select>
                                </div>

                                <div class="flex flex-col space-y-1">
                                    <label for="doors" class="text-sm font-semibold text-gray-500">Doors</label>
                                    <select id="doors" class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                    </select>
                                </div>

                                <div class="flex flex-col space-y-1">
                                    <label for="dwheels" class="text-sm font-semibold text-gray-500">Drive wheels</label>
                                    <select id="dwheels" class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                    </select>
                                </div>

                                <div class="flex flex-col space-y-1">
                                    <label for="wheel" class="text-sm font-semibold text-gray-500">Wheel</label>
                                    <select id="wheel" class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                    </select>
                                </div>

                                <div class="flex flex-col space-y-1">
                                    <label for="airbag" class="text-sm font-semibold text-gray-500">Airbags</label>
                                    <select id="airbag" class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                    </select>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Image selector -->
            <div class="flex items-center justify-center">
                <div class="p-4 md:mt-0 mt-20 w-[800px]">
                    <div class="flex bg-[#E6E6E6] rounded-md shadow-4xl md:flex-row">
                        <div class="p-5 w-full">
                            <h3 class="my-4 text-2xl font-semibold text-gray-700 uppercase text-center">Image selector</h3>
                            <div class="">
                                <div class="font-[sans-serif] mt-2 mb-12">
                                    <input 
                                        type="file" 
                                        ref="file" 
                                        multiple
                                        @change="onFileChange"
                                        class="w-full text-black text-sm bg-gray-100 file:cursor-pointer cursor-pointer file:border-0 file:py-2 file:px-4 file:mr-4 file:bg-gray-800 file:hover:bg-gray-700 file:text-white rounded" />
                                </div>
                            </div>
                            <div id="preview" v-if="url && url.length > 0" class="w-full h-auto grid md:grid-cols-3 grid-cols-2 lg:grid-cols-5 gap-x-6">
                                <img v-for="(imageUrl, index) in url" :key="index" :src="imageUrl" class="w-full md:h-auto h-[80%] border-2 border-black" @click="handleImageClick(imageUrl)">
                            
                            </div>

                            <div v-if="mainImage" class="flex flex-col justify-center items-center">
                                <h1 class="mt-10 uppercase text-2xl">Main image</h1>
                                <div class="w-full mt-10 flex justify-center items-center">
                                    <img :src="mainImage" class="w-[80%] rounded-lg shadow-lg" alt="Main Image">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Other -->
            <div class="flex items-center justify-center">
                <div class="p-4 md:mt-0 mt-20 w-[800px]">
                    <div class="flex bg-[#E6E6E6] rounded-md shadow-4xl md:flex-row ">
                        <div class="p-5 w-full">
                            <h3 class="my-4 text-2xl font-semibold text-gray-700 uppercase text-center">Other</h3>
                            <p class="text-gray-600 ml-2 mb-4 text-lg uppercase font-bold">car color</p>
                                <div class="flex justify-center items-center">
                                    <div class="grid xl:grid-cols-5 lg:grid-cols-5 md:grid-cols-4 sm:grid-cols-4 grid-cols-2 gap-10">
                                        <div class="" v-for="(color, index) in colors" :key="index">
                                            <button :class="getCarColor(color)" @click.prevent="handleColorClick(color)">{{ color }}</button>
                                        </div>
                                    </div>
                                </div>
                                <hr class="mt-[30px] text-black bg-black h-0.5" />
                            <p class="text-gray-600 ml-2 mb-4 text-lg uppercase font-bold mt-10">interior material and colors</p>
                            <div class="flex justify-center items-center">
                                    <div class="grid xl:grid-cols-3 lg:grid-cols-3 md:grid-cols-3 sm:grid-cols-3 grid-cols-1 gap-10 mb-20 mt-10">
                                        <div class="" v-for="(material, index) in materials" :key="index">
                                            <button :class="getMaterialInterior(material)" @click.prevent="handleMaterialClick(material)" class="w-44 text-sm text-white rounded-full uppercase py-2 bg-[#222]" >{{ material }}</button>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex justify-center items-center">
                                    <div class="grid xl:grid-cols-5 lg:grid-cols-5 md:grid-cols-4 sm:grid-cols-4 grid-cols-2 gap-10">
                                        <div class="" v-for="(color, index) in materialColors" :key="index">
                                            <button :class="getMaterialColor(color)" @click.prevent="handleMaterialColorClick(color)">{{ color }}</button>
                                        </div>
                                    </div>
                                </div>
                            <hr class="mt-[30px] text-black bg-black h-0.5" />
                                
                            <div>
                                <button 
                                    class="btn2 w-full mt-20 px-10 py-5 text-lg relative transition-colors border border-black rounded-md uppercase font-semibold tracking-wider leading-none overflow-hidden hover:text-white" 
                                    type="submit"
                                    >
                                    <span class="absolute inset-0 bg-[#222]"></span>
                                    <span class="absolute inset-0 flex justify-center items-center font-bold">ADD</span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import { RouterLink } from 'vue-router'
import Trans from '@/i18n/translation'
export default {
  setup() {
    return {
      Trans
    }
  },
  data() {
    return {
      colors: ['black', 'blue', 'red', 'white', 'green', 'brown', 'yellow', 'purple', 'orange', 'gray'],
      selectedColor: null,
      materialColors: ['black', 'red', 'white', 'brown', 'gray'],
      materialColorSelected: null,
      materials: ['alcantara', 'artificial', 'combined', 'leather', 'fabric'],
      selectedMaterial: null,
      url: null,
      selectedImage: null,
    };
  },
  computed: {
        mainImage() {
            return this.selectedImage || (this.url && this.url.length > 0 && this.url[0]) || null;
        }
    },
  methods: {
    onFileChange(e) {
        const files = e.target.files;
        const urls = [];
        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            const url = URL.createObjectURL(file);
            urls.push(url);
        }
        this.url = urls;
    },
    handleImageClick(imageUrl) {
        // Set the clicked image as the selected image
        this.selectedImage = imageUrl;
    },

    getCarColor(color) {
        let baseClass = 'py-2 w-24 rounded-full uppercase';
        if (color === 'black') {
            return `${baseClass} ${this.selectedColor === 'black' ? 'border-green-500 border-2 bg-black text-white' : 'bg-black text-white'}`;
        } else if (color === 'blue') {
            return `${baseClass} ${this.selectedColor === 'blue' ? 'border-green-500 border-2 bg-blue-700 text-white' : 'bg-blue-700 text-white'}`;
        } else if (color === 'red') {
            return `${baseClass} ${this.selectedColor === 'red' ? 'border-green-500 border-2 bg-red-600 text-white' : 'bg-red-600 text-white'}`;
        } else if (color === 'white') {
            return `${baseClass} ${this.selectedColor === 'white' ? 'border-green-500 border-2 bg-white text-black' : 'bg-white text-black'}`;
        } else if (color === 'green') {
            return `${baseClass} ${this.selectedColor === 'green' ? 'border-green-500 border-2 bg-green-700 text-white' : 'bg-green-700 text-white'}`;
        } else if (color === 'brown') {
            return `${baseClass} ${this.selectedColor === 'brown' ? 'border-green-500 border-2 bg-[#a52a2a] text-white' : 'bg-[#a52a2a] text-white'}`;
        } else if (color === 'yellow') {
            return `${baseClass} ${this.selectedColor === 'yellow' ? 'border-green-500 border-2 bg-yellow-400 text-black' : 'bg-yellow-400 text-black'}`;
        } else if (color === 'purple') {
            return `${baseClass} ${this.selectedColor === 'purple' ? 'border-green-500 border-2 bg-purple-600 text-white' : 'bg-purple-600 text-white'}`;
        } else if (color === 'orange') {
            return `${baseClass} ${this.selectedColor === 'orange' ? 'border-green-500 border-2 bg-orange-500 text-white' : 'bg-orange-500 text-white'}`;
        } else if (color === 'gray') {
            return `${baseClass} ${this.selectedColor === 'gray' ? 'border-green-500 border-2 bg-gray-500 text-white' : 'bg-gray-500 text-white'}`;
        }
    },
    getMaterialColor(color) {
        let baseClass = 'py-2 w-24 rounded-full uppercase';
        if (color === 'black') {
            return `${baseClass} ${this.materialColorSelected === 'black' ? 'border-green-500 border-2 bg-black text-white' : 'bg-black text-white'}`;
        } else if (color === 'red') {
            return `${baseClass} ${this.materialColorSelected === 'red' ? 'border-green-500 border-2 bg-red-600 text-white' : 'bg-red-600 text-white'}`;
        } else if (color === 'white') {
            return `${baseClass} ${this.materialColorSelected === 'white' ? 'border-green-500 border-2 bg-white text-black' : 'bg-white text-black'}`;
        } else if (color === 'brown') {
            return `${baseClass} ${this.materialColorSelected === 'brown' ? 'border-green-500 border-2 bg-[#a52a2a] text-white' : 'bg-[#a52a2a] text-white'}`;
        } else if (color === 'gray') {
            return `${baseClass} ${this.materialColorSelected === 'gray' ? 'border-green-500 border-2 bg-gray-500 text-white' : 'bg-gray-500 text-white'}`;
        }
    },
    getMaterialInterior(material) {
    let baseClass = 'py-2 w-44 rounded-full uppercase';
    if (material === this.selectedMaterial) {
        return `${baseClass} border-green-500 border-2 bg-[#222] text-white`;
    } else {
        return `${baseClass} bg-[#222] text-white`;
    }
    },

    handleMaterialClick(material) {
        this.selectedMaterial = material;
    },

    handleMaterialColorClick(color) {
        this.materialColorSelected = color;
    },
    handleColorClick(color) {
      console.log(`You clicked on ${color}`);
      this.selectedColor = color;
    },
  }
}
</script>


<style scoped>
.shadow-4xl {
    --tw-shadow: 0 50px 100px -20px rgba(0, 0, 0, 0.4);
    --tw-shadow-colored: 0 50px 100px -20px var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}
.btn2 span:first-child{
  transform: translateX(-101%);
  transition: transform .3s ease-in
}
.btn2:hover span{
  transform: translateX(0)
}
</style>