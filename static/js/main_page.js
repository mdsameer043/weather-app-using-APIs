let a, i, n;

//const options1 = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
const options1 = { year: 'numeric', month: 'long' };
const options2 = { weekday: 'long' };
a = new Date();
if (a.getHours() >= 12) {
    i = "Pm";
}
else {
    i = "Am";
}
setInterval(() => {
    n = new Date();
    date.innerHTML = n.toLocaleDateString(undefined, options1);
    day.innerHTML = n.toLocaleDateString(undefined, options2);
    time.innerHTML = n.getHours() + ':' + n.getMinutes() + ' ' + i;
}, 1000)



b = new Date();
let myhour = b.getHours();
if (myhour <= 6 || myhour >= 18) {
    //white clouds 
    document.getElementById("cloud1_image").style.visibility = "hidden";
    document.getElementById("cloud2_image").style.visibility = "hidden";
    document.getElementById("cloud3_image").style.visibility = "hidden";
    document.getElementById("cloud4_image").style.visibility = "hidden";
    document.getElementById("cloud5_image").style.visibility = "hidden";

    //black clouds
    document.getElementById("blackcloud6_image").style.visibility = "visible";
    document.getElementById("blackcloud7_image").style.visibility = "visible";
    document.getElementById("blackcloud8_image").style.visibility = "visible";
    document.getElementById("blackcloud9_image").style.visibility = "visible";
    document.getElementById("blackcloud10_image").style.visibility = "visible";
    // document.getElementById("skyimage").src = "{{url_for('static',filename='resources/img/nightsky2.jpg')}}";


    document.getElementById("skyimage").src = "static/resources/img/nightsky2.jpg";

    
    // document.getElementById("sunimage").src = "{{url_for('static',filename='resources/img/halfmoon1.png')}}";
    document.getElementById("weather_mood").style.color = "white";
    document.getElementById("boxday").style.color = "white";
    document.getElementById("boxdate").style.color = "white";
    document.getElementById("boxtime").style.color = "white";
    document.getElementById("boxtemp").style.color = "white";
    document.getElementById("boxhumidity").style.color = "white";
    document.getElementById("boxwindspeed").style.color = "white";
    document.getElementById("boxfeelslike").style.color = "white";
    document.getElementById("boxwinddegrees").style.color = "white";
    document.getElementById("boxcity").style.color = "white";
    document.getElementById("hourly_data_button").style.color = "white";
    document.getElementById("daily_data_button").style.color = "white";
    document.getElementById("forcast_heading_gap").style.color = "white";

}

else{
    //white clouds 
    document.getElementById("cloud1_image").style.visibility = "visible";
    document.getElementById("cloud2_image").style.visibility = "visible";
    document.getElementById("cloud3_image").style.visibility = "visible";
    document.getElementById("cloud4_image").style.visibility = "visible";
    document.getElementById("cloud5_image").style.visibility = "visible";

    //black clouds
    document.getElementById("blackcloud6_image").style.visibility = "hidden";
    document.getElementById("blackcloud7_image").style.visibility = "hidden";
    document.getElementById("blackcloud8_image").style.visibility = "hidden";
    document.getElementById("blackcloud9_image").style.visibility = "hidden";
    document.getElementById("blackcloud10_image").style.visibility = "hidden";
    }

//hello world


//document.getElementById("sunimage").src = "{{url_for('static',filename='halfmoon1.png')}}"; //cloudy mood


//document.getElementById("skyimage").src = "{{url_for('static',filename='nightsky2.jpg')}}"; //cloudy mood



// const url ="https://weather-by-api-ninjas.p.rapidapi.com/v1/weather?city=Dappur";
// const options = {
//     method: "GET",
//     headers: {
//         "X-RapidAPI-Key": "ea77a70441msh0f1a928a9888502p13bdbbjsncaf20ee225b5",
//         "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com",
//     }
// };

// const getWeather = (city) => {
//     cityname.innerHTML = city;
//     fetch("https://weather-by-api-ninjas.p.rapidapi.com/v1/weather?city=" + city, options)
//         .then((response) => response.json())
//         .then((response) => {
//             console.log(response);
//             temp.innerHTML = response.temp;
//             //temp2.innerHTML = response.temp;
//             //max_temp.innerHTML = response.max_temp;
//             //min_temp.innerHTML = response.min_temp;
//             //sunrise.innerHTML = response.sunrise;
//             //sunset.innerHTML = response.sunset;
//             cloud_pct = response.cloud_pct;
//             feels_like.innerHTML = response.feels_like;
//             humidity.innerHTML = response.humidity;
//             //humidity2.innerHTML = response.humidity;
//             wind_speed.innerHTML = response.wind_speed;
//             //wind_speed2.innerHTML = response.wind_speed;
//             wind_degrees.innerHTML = response.wind_degrees;
//         })
//         .catch((err) => console.error(err));
// };

// submit.addEventListener("click", (e) => {
//     e.preventDefault();
//     getWeather(input.value);
// });
// getWeather("Dappur");





document.getElementById("submit_id_main_page").addEventListener("click",()=>{
    let val=document.querySelector("#input_query_main_page").value;
    document.querySelector("#city_query").value = val;
    document.forms.city_from.submit();
})


// hourly and monthly buttons for changing forcast data 
document.getElementById("hourly_data_button").addEventListener("click",()=>{
    document.getElementById("forcast_type_query_id").value = "hourly";
    document.forms.forcast_type.submit();
})
document.getElementById("daily_data_button").addEventListener("click",()=>{
    document.getElementById("forcast_type_query_id").value = "daily";
    document.forms.forcast_type.submit();
})






let day_spacing = new Date().toLocaleString('en-us', {  weekday: 'long' });

console.log(day_spacing)
if (day_spacing == "Wednesday"){
    document.getElementById("boxdate").style.left = "26vw";
}
else if(day_spacing == "Tuesday"){
    document.getElementById("boxdate").style.left = "22vw";
}
else if(day_spacing == "Thursday"){
    document.getElementById("boxdate").style.left = "23vw";
}
else if(day_spacing == "Saturday"){
    document.getElementById("boxdate").style.left = "23vw";
}
else{
    document.getElementById("boxdate").style.left = "21vw";
}


var weatherMood = document.getElementById("weather_mood").innerHTML;

if (myhour <= 6 || myhour >= 18){
    document.getElementById("sunimage").src = "static/resources/img/halfmoon1.png";
}
else{
    if(weatherMood=="Clear"){
    document.getElementById("sunimage").src = "static/resources/img/sun2.png";
    }
    else if(weatherMood=="Mostly Cloudy"){
        document.getElementById("sunimage").src = "static/resources/img/sunclound1.png";
    }
    else if(weatherMood=="Partly Cloudy"){
        document.getElementById("sunimage").src = "static/resources/img/sunclound1.png";
    }
    else if(weatherMood=="Overcast"){
        document.getElementById("sunimage").src = "static/resources/img/sunrainnycloud.png";
    }
    else if(weatherMood=="Foggy"){
        document.getElementById("sunimage").src = "static/resources/img/cloudy2.png";
    }
    else if(weatherMood=="Breezy and Overcast"){
        document.getElementById("sunimage").src = "static/resources/img/sunclound1.png";
    }
    else if(weatherMood=="Breezy and Partly Cloudy"){
        document.getElementById("sunimage").src = "static/resources/img/sunclound1.png";
    }
    else if(weatherMood=="Breezy and Mostly Cloudy"){
        document.getElementById("sunimage").src = "static/resources/img/sunclound1.png";
    }
    else{
        document.getElementById("sunimage").src = "static/resources/img/sun2.png";
    }

}
