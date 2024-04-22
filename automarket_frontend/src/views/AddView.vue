<template>
    <div class="md:pt-40 pt-14">
        <h1 class="text-center mb-12 mt-10 text-4xl uppercase">add car</h1>
        <form @submit.prevent="submitCarForm" action="#" class="flex md:flex-col flex-col space-y-5">
            <!-- Main specifications -->
            <div class="flex items-center justify-center">
                <div class="p-4 md:mt-0 mt-20 w-[800px]">
                    <div class="flex bg-[#E6E6E6] rounded-md shadow-4xl md:flex-row ">
                        <div class="p-5 w-full">
                            <h3 class="my-4 text-2xl font-semibold text-gray-700 uppercase text-center">main specifications</h3>
                            <div class="grid md:grid-cols-3 gird-cols-1 gap-4">
                                <!-- MANUFACTURERS -->
                                <div class="flex flex-col space-y-1">
                                    <label for="manufacturer" class="text-sm font-semibold text-gray-500">Manufacturer</label>
                                    <select v-model="selectedManufacturer" id="manufacturer" class="px-2 py-2 uppercase text-sm transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                        <option disabled>Choose manufacturer</option>
                                        <option 
                                            v-for="(manufacturerName, index) in choices.manufacturer"
                                            :key="index"
                                            :value="manufacturerName"
                                        >
                                            {{ manufacturerName }}
                                        </option>
                                    </select>
                                </div>
                                <!-- MODELS -->
                                <div class="flex flex-col space-y-1">
                                    <label for="model" class="text-sm font-semibold text-gray-500">Model</label>
                                    <select 
                                        v-model="selectedCarModel" 
                                        id="model" class="px-4 py-2 uppercase text-sm transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black"
                                        >
                                        <option disabled>Choose model</option>
                                        <option
                                            v-for="model  in carModels"
                                            :key="model"
                                            :value="model"
                                        >
                                            {{ model }}
                                        </option>
                                    </select>
                                </div>
                                <!-- CATEGORIES -->
                                <div class="flex flex-col space-y-1">
                                    <label for="category" class="text-sm font-semibold text-gray-500">Category</label>
                                    <select v-model="selectedCategories" id="category" class="px-4 uppercase text-sm py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                        <option disabled>Choose category</option>
                                        <option
                                            v-for="(category, index) in choices.categories"
                                            :key="index"
                                            :value="category"
                                        >
                                            {{ category }}
                                        </option>
                                    </select>
                                </div>
                                <!-- TYPES -->
                                <div class="flex flex-col space-y-1">
                                    <label for="type" class="text-sm font-semibold text-gray-500">Type</label>
                                    <select v-model="selectedType" id="type" class="px-4 py-2 uppercase text-sm transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                        <option disabled>Choose type</option>
                                        <option 
                                            v-for="(type, index) in choices.types"
                                            :key="index"
                                            :value="type"
                                        >
                                            {{ type }}
                                        </option>
                                    </select>
                                </div>
                                <!-- YEAR -->
                                <div class="flex flex-col space-y-1">
                                    <label for="year" class="text-sm font-semibold text-gray-500">Year</label>
                                    <input v-model="year" placeholder="Enter year" type="number" id="year" class="placeholder-gray-500 uppercase text-sm border border-gray-300 text-black bg-white px-4 rounded py-2 outline-none" />
                                </div>
                                <!-- PRICE -->
                                <div class="flex flex-col space-y-1">
                                    <label for="price" class="text-sm font-semibold text-gray-500">Price</label>
                                    <input v-model="price" placeholder="Enter year" type="number" id="price" class="placeholder-gray-500 uppercase text-sm border border-gray-300 text-black bg-white px-4 rounded py-2 outline-none" />
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
                                <!-- LOCATION -->
                                <div class="flex flex-col space-y-1">
                                    <label for="location" class="text-sm font-semibold text-gray-500">Location</label>
                                    <select v-model="selectedLocation" id="location" class="px-4 py-2 transition duration-300 border uppercase text-sm border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                        <option disabled>Choose location</option>
                                        <option
                                            v-for="(loc, index) in choices.location"
                                            :key="index"
                                            :value="loc"
                                        >
                                            {{ loc }}
                                        </option>
                                    </select>
                                </div>
                                <!-- ENGINE VOLUME -->
                                <div class="flex flex-col space-y-1">
                                    <label for="enginev" class="text-sm font-semibold text-gray-500">Engine volume</label>
                                    <input v-model="engineVolume" placeholder="Engine volume" type="number" id="enginev" class="placeholder-gray-500 border uppercase text-sm border-gray-300  cursor-pointer text-black bg-white px-4 rounded py-2 outline-none" />
                                </div>
                                <!-- MILAGE -->
                                <div class="flex flex-col space-y-1">
                                    <label for="milage" class="text-sm font-semibold text-gray-500">Milage km</label>
                                    <input v-model="milage" placeholder="Enter milage" type="number" id="milage" class="placeholder-gray-500 border text-sm uppercase border-gray-300  cursor-pointer text-black bg-white px-4 rounded py-2 outline-none" />
                                </div>
                                <!-- FUEL TYPE -->
                                <div class="flex flex-col space-y-1">
                                    <label for="fuel" class="text-sm font-semibold text-gray-500">Fuel type</label>
                                    <select v-model="selectedFuelTypes" id="fuel" class="px-4 py-2 transition uppercase text-sm duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                        <option disabled>Choose fuel type</option>
                                        <option
                                            v-for="(fuel, index) in choices.fuel_type"
                                            :key="index"
                                            :value="fuel"
                                        >
                                            {{ fuel }}
                                        </option>
                                    </select>
                                </div>
                                <!-- TRANSMISSION -->
                                <div class="flex flex-col space-y-1">
                                    <label for="transmission" class="text-sm font-semibold text-gray-500">Transmission</label>
                                    <select  v-model="selectedTransmission"  id="transmission" class="px-4 py-2 uppercase text-sm transition duration-300 border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                        <option disabled>Choose transmission type</option>
                                        <option 
                                            v-for="(trans, index) in choices.transmission"
                                            :key="index"
                                            :value="trans"
                                        >
                                            {{ trans }}
                                        </option>
                                    </select>
                                </div>
                                <!-- CYLINDERS -->
                                <div class="flex flex-col space-y-1">
                                    <label for="cylinders" class="text-sm font-semibold text-gray-500">Cylinders</label>
                                    <select v-model="selectedCylinders" id="cylinders" class="px-4 py-2 transition duration-300 uppercase text-sm border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                        <option disabled>Choose cylinders quantity</option>
                                        <option 
                                            v-for="(cylinder, index) in choices.cylinders"
                                            :key="index"
                                            :value="cylinder"
                                        >
                                            {{ cylinder }}
                                        </option>
                                    </select>
                                </div>
                                <!-- DOORS -->
                                <div class="flex flex-col space-y-1">
                                    <label for="doors" class="text-sm font-semibold text-gray-500">Doors</label>
                                    <select v-model="selectedDoors" id="doors" class="px-4 py-2 transition duration-300 uppercase text-sm border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                        <option disabled>Choose doors quantity</option>
                                        <option 
                                            v-for="(door, index) in choices.doors"
                                            :key="index"
                                            :value="door"
                                        >
                                            {{ door }}
                                        </option>
                                    </select>
                                </div>
                                <!-- DRIVE WHEELS -->
                                <div class="flex flex-col space-y-1">
                                    <label for="dwheels" class="text-sm font-semibold text-gray-500">Drive wheels</label>
                                    <select v-model="selectedDriveWheels" id="dwheels" class="px-4 py-2 transition duration-300 uppercase text-sm border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                        <option disabled>Choose drive wheels</option>
                                        <option 
                                            v-for="(driveWheel, index) in choices.drive_wheels"
                                            :key="index"
                                            :value="driveWheel"
                                        >
                                            {{ driveWheel }}
                                        </option>
                                    </select>
                                </div>
                                <!-- WHEEL -->
                                <div class="flex flex-col space-y-1">
                                    <label for="wheel" class="text-sm font-semibold text-gray-500">Wheel</label>
                                    <select v-model="selectedWheel" id="wheel" class="px-4 py-2 transition duration-300 uppercase text-sm border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                        <option disabled>Choose wheel side</option>
                                        <option 
                                            v-for="(whl, index) in choices.wheel"
                                            :key="index"
                                            :value="whl"
                                        >
                                            {{ whl }}
                                        </option>
                                    </select>
                                </div>

                                <div class="flex flex-col space-y-1">
                                    <label for="airbag" class="text-sm font-semibold text-gray-500">Airbags</label>
                                    <select v-model="selectedAirbags" id="airbag" class="px-4 py-2 transition duration-300 uppercase text-sm border border-gray-300 rounded focus:border-transparent focus:ring-1 focus:outline-none focus:ring-black">
                                        <option disabled>Choose airbags quantity</option>
                                        <option 
                                            v-for="(airbag, index) in choices.airbags"
                                            :key="index"
                                            :value="airbag"
                                        >
                                            {{ airbag }}
                                        </option>
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
                                        name="images"
                                        @change="onFileChange"
                                        class="w-full text-black text-sm bg-gray-100 file:cursor-pointer cursor-pointer file:border-0 file:py-2 file:px-4 file:mr-4 file:bg-gray-800 file:hover:bg-gray-700 file:text-white rounded" 
                                    />
                                </div>
                            </div>
                            <div id="preview" v-if="url && url.length > 0" class="w-full h-auto grid md:grid-cols-3 grid-cols-2 lg:grid-cols-5 gap-x-6">
                                <img v-for="(imageUrl, index) in url" :key="index" :src="imageUrl" class="w-full md:h-32 h-[80%] border-2 border-black" @click="handleImageClick(imageUrl)">
                            
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
                                        <div class="" v-for="(color, index) in choices.car_colors" :key="index">
                                            <button :class="getCarColor(color)" @click.prevent="handleColorClick(color)">{{ color }}</button>
                                        </div>
                                    </div>
                                </div>
                                <hr class="mt-[30px] text-black bg-black h-0.5" />
                            <p class="text-gray-600 ml-2 mb-4 text-lg uppercase font-bold mt-10">interior material and colors</p>
                            <div class="flex justify-center items-center">
                                    <div class="grid xl:grid-cols-3 lg:grid-cols-3 md:grid-cols-3 sm:grid-cols-3 grid-cols-1 gap-10 mb-20 mt-10">
                                        <div class="" v-for="(material, index) in choices.interior" :key="index">
                                            <button :class="getMaterialInterior(material)" @click.prevent="handleMaterialClick(material)" class="w-44 text-sm text-white rounded-full uppercase py-2 bg-[#222]" >{{ material }}</button>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex justify-center items-center">
                                    <div class="grid xl:grid-cols-5 lg:grid-cols-5 md:grid-cols-4 sm:grid-cols-4 grid-cols-2 gap-10">
                                        <div class="" v-for="(color, index) in choices.interior_color" :key="index">
                                            <button :class="getMaterialColor(color)" @click.prevent="handleMaterialColorClick(color)">{{ color }}</button>
                                        </div>
                                    </div>
                                </div>
                            <hr class="mt-[30px] text-black bg-black h-0.5" />
                            <!-- Description -->
                            <div class="mt-8">
                                <label for="description" class="text-gray-600 ml-2 mb-4 text-lg uppercase font-bold mt-10">DESCRIPTION</label>
                                <textarea v-model="description" placeholder="Write description" type="text" id="description" class="placeholder-gray-500 mt-4 border min-h-52 w-full border-gray-300 cursor-pointer text-black bg-[#E6E6E6] shadow-2xl px-4 rounded-lg py-2 outline-none" style="resize: none;"></textarea>
                            </div>
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
import Trans from '@/i18n/translation'
import axios from 'axios';
export default {
  setup() {
    return {
      Trans
    }
  },
  data() {
    return {
      url: null,
      selectedMainImage: null,
      selectedImages: [],
      selectedManufacturer: 'Choose manufacturer',
      selectedCarModel: 'Choose model',
      selectedCategories: 'Choose category',
      selectedType: 'Choose type',
      selectedLocation: 'Choose location',
      selectedFuelTypes: 'Choose fuel type',
      selectedTransmission: 'Choose transmission type',
      selectedCylinders: 'Choose cylinders quantity',
      selectedDoors: 'Choose doors quantity',
      selectedDriveWheels: 'Choose drive wheels',
      selectedWheel: 'Choose wheel side',
      selectedAirbags: 'Choose airbags quantity',
      carColors: null,
      interior: null,
      interiorColor: null,
      year: null,
      price: null,
      milage: null,
      description: null,
      engineVolume: null,
      choices: {
        manufacturer: [],
        car_model: {},
        categories: [],
        types: [],
        location: [],
        fuel_type: [],
        transmission: [],
        cylinders: [],
        doors: [],
        drive_wheels: [],
        wheel: [],
        airbags: [],
        car_colors: [],
        interior: [],
        interior_color: []
      },
      carModels: []
    };
  },
  watch: {
    selectedManufacturer(newVal, oldVal) {
      if (newVal !== oldVal) {
        this.updateCarModels();
      }
    }
  },
  created() {
    this.fetchChoices()
  },
  computed: {
    // Choosing main image from uploaded images
        mainImage() {
            return this.selectedMainImage || (this.url && this.url.length > 0 && this.url[0]) || null;
        }
    },
  methods: {
    // Fetching choices from server
    fetchChoices() {
        axios
            .get('/api/choices')
            .then(response => {
                console.log(response.data)
                this.choices = response.data
            })
            .catch(error => {
                console.log('error: ',error)
            })
    },
    // Updating car models based on manufacturers
    updateCarModels() {
        if (this.selectedManufacturer && this.choices.car_model[this.selectedManufacturer]){
            this.carModels = this.choices.car_model[this.selectedManufacturer]
        }
    },
    submitCarForm() {
    // Send forms to backend
    let formData = new FormData();
    formData.append('manufacturer', this.selectedManufacturer);
    formData.append('car_model', this.selectedCarModel);
    formData.append('types', this.selectedType);
    formData.append('categories', this.selectedCategories);
    formData.append('price', this.price);
    formData.append('year', this.year);
    formData.append('location', this.selectedLocation);
    formData.append('engine_volume', this.engineVolume);
    formData.append('milage', this.milage);
    formData.append('fuel_type', this.selectedFuelTypes);
    formData.append('transmission', this.selectedTransmission);
    formData.append('cylinders', this.selectedCylinders);
    formData.append('doors', this.selectedDoors);
    formData.append('drive_wheels', this.selectedDriveWheels);
    formData.append('wheel', this.selectedWheel);
    formData.append('airbags', this.selectedAirbags);
    formData.append('car_colors', this.carColors);
    formData.append('interior', this.interior);
    formData.append('interior_color', this.interiorColor);
    formData.append('description', this.description);

    // Send all images which is uploaded to backend
    console.log('Selected images before appending:', this.selectedImages);
    if (this.selectedImages && this.selectedImages.length > 0) {
        for (let i = 0; i < this.selectedImages.length; i++) {
            formData.append('images[]', this.selectedImages[i]);
        }
    } else {
        console.log('No images selected or selectedImages is undefined.');
        return;
    }
    // Fetch blob to url and send backend
    if (this.mainImage) {
        fetch(this.mainImage)
            .then(res => res.blob())
            .then(blob => {
                const mainImageFile = new File([blob], 'main_image.jpg', { type: 'image/jpeg' });
                formData.append('main_image', mainImageFile);
                console.log('Main image file appended:', mainImageFile);

                axios.post('/api/create/', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.error('Error submitting form:', error);
                });
            });
        } else {
         console.log('Error: Main image is not sent');
        }
    },
    onFileChange(e) {
        console.log('onFileChange triggered')
        if (e.target.files.length > 0) {
            console.log('Files selected:', e.target.files);
            const files = e.target.files;
            const urls = []
            this.selectedImages = []
            for (let i = 0; i < files.length; i++) {
                const file = files[i]
                const url = URL.createObjectURL(file)
                urls.push(url)
                this.selectedImages.push(file)
            }
            this.url = urls;
            console.log('File URLs:', this.url)
        } else {
            console.log('No files selected.')
        }
    },
    handleImageClick(imageUrl) {
        this.selectedMainImage = imageUrl;
    },
    // Adding styles based fetched car colors from backend
    getCarColor(color) {
        let baseClass = 'py-2 w-24 rounded-full uppercase';
        if (color === 'Black') {
            return `${baseClass} ${this.carColors === 'Black' ? 'border-green-500 border-2 bg-black text-white' : 'bg-black text-white'}`;
        } else if (color === 'Blue') {
            return `${baseClass} ${this.carColors === 'Blue' ? 'border-green-500 border-2 bg-blue-700 text-white' : 'bg-blue-700 text-white'}`;
        } else if (color === 'Red') {
            return `${baseClass} ${this.carColors === 'Red' ? 'border-green-500 border-2 bg-red-600 text-white' : 'bg-red-600 text-white'}`;
        } else if (color === 'White') {
            return `${baseClass} ${this.carColors === 'White' ? 'border-green-500 border-2 bg-white text-black' : 'bg-white text-black'}`;
        } else if (color === 'Green') {
            return `${baseClass} ${this.carColors === 'Green' ? 'border-green-500 border-2 bg-green-700 text-white' : 'bg-green-700 text-white'}`;
        } else if (color === 'Brown') {
            return `${baseClass} ${this.carColors === 'Brown' ? 'border-green-500 border-2 bg-[#a52a2a] text-white' : 'bg-[#a52a2a] text-white'}`;
        } else if (color === 'Yellow') {
            return `${baseClass} ${this.carColors === 'Yellow' ? 'border-green-500 border-2 bg-yellow-400 text-black' : 'bg-yellow-400 text-black'}`;
        } else if (color === 'Purple') {
            return `${baseClass} ${this.carColors === 'Purple' ? 'border-green-500 border-2 bg-purple-600 text-white' : 'bg-purple-600 text-white'}`;
        } else if (color === 'Orange') {
            return `${baseClass} ${this.carColors === 'Orange' ? 'border-green-500 border-2 bg-orange-500 text-white' : 'bg-orange-500 text-white'}`;
        } else if (color === 'Gray') {
            return `${baseClass} ${this.carColors === 'Gray' ? 'border-green-500 border-2 bg-gray-500 text-white' : 'bg-gray-500 text-white'}`;
        }
    },
    // Adding styles based fetched car material colors from backend
    getMaterialColor(color) {
        let baseClass = 'py-2 w-24 rounded-full uppercase';
        if (color === 'Black') {
            return `${baseClass} ${this.interiorColor === 'Black' ? 'border-green-500 border-2 bg-black text-white' : 'bg-black text-white'}`;
        } else if (color === 'Red') {
            return `${baseClass} ${this.interiorColor === 'Red' ? 'border-green-500 border-2 bg-red-600 text-white' : 'bg-red-600 text-white'}`;
        } else if (color === 'White') {
            return `${baseClass} ${this.interiorColor === 'White' ? 'border-green-500 border-2 bg-white text-black' : 'bg-white text-black'}`;
        } else if (color === 'Brown') {
            return `${baseClass} ${this.interiorColor === 'Brown' ? 'border-green-500 border-2 bg-[#a52a2a] text-white' : 'bg-[#a52a2a] text-white'}`;
        } else if (color === 'Gray') {
            return `${baseClass} ${this.interiorColor === 'Gray' ? 'border-green-500 border-2 bg-gray-500 text-white' : 'bg-gray-500 text-white'}`;
        }
    },
    // Adding styles based fetched car materials from backend
    getMaterialInterior(material) {
    let baseClass = 'py-2 w-44 rounded-full uppercase';
    if (material === this.interior) {
        return `${baseClass} border-green-500 border-2 bg-[#222] text-white`;
    } else {
        return `${baseClass} bg-[#222] text-white`;
    }
    },

    handleMaterialClick(material) {
        this.interior = material;
    },

    handleMaterialColorClick(color) {
        this.interiorColor = color;
    },
    handleColorClick(color) {
        this.carColors = color;
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