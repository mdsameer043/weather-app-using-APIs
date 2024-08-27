    //animation start
    let h1 = new Date().getHours();
    //let h1=2
    if (h1 <= 6 || h1 >= 18) {
      document.body.style.backgroundImage = "url('static/resources/img/nightsky2.jpg')"
      headday.style.color = "white";
      headdate.style.color = "white";
      headtime.style.color = "white";
      headweather.style.color = "white";
      bodyweather.style.color = "white";
      oner.style.color = "white";
    }
    //animation ends




    //Date function start
    let current_time, Am_PM_indicator, n, h;
    //const options1 = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    const options1 = { year: 'numeric', month: 'long' };
    const options2 = { weekday: 'long' };
    current_time = new Date();
    if (current_time.getHours() >= 12) {
      Am_PM_indicator = "Pm";
    }
    else {
      Am_PM_indicator = "Am";
    }
    setInterval(() => {
      n = new Date();
      h = n.getHours();
      if (h > 12) {
        h = h - 12;
      }
      date.innerHTML = n.toLocaleDateString(undefined, options1);
      day.innerHTML = n.toLocaleDateString(undefined, options2);
      time.innerHTML = h + ':' + n.getMinutes() + ' ' + Am_PM_indicator;
    }, 1000)
    // Date function end







    //api request method start
    // const url ="https://weather-by-api-ninjas.p.rapidapi.com/v1/weather?city=Dappur";
    // const options = {
    //   method: "GET",
    //   headers: {
    //     "X-RapidAPI-Key": "ea77a70441msh0f1a928a9888502p13bdbbjsncaf20ee225b5",
    //     "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com",
    //   }
    // };

    // const getWeather = (city) => {
    //   cityname.innerHTML = city;
    //   fetch("https://weather-by-api-ninjas.p.rapidapi.com/v1/weather?city=" + city, options)
    //     .then((response) => response.json())
    //     .then((response) => {
    //       console.log(response);
    //       temp.innerHTML = response.temp;
    //       temp2.innerHTML = response.temp;
    //       max_temp.innerHTML = response.max_temp;
    //       min_temp.innerHTML = response.min_temp;

    //       var unix_timestamp = response.sunrise;
    //       var date = new Date(unix_timestamp * 1000);
    //       var hours = date.getHours();
    //       if(hours>12){hours=hours-12}
    //       var minutes = "0" + date.getMinutes();
    //       var seconds = "0" + date.getSeconds();
    //       var formattedTime = hours + ':' + minutes.substr(-2) + ' ' + 'am';
    //       sunrise.innerHTML = formattedTime;
    //       //sunrise.innerHTML = response.sunrise;

    //       var unix_timestamp = response.sunset;
    //       var date = new Date(unix_timestamp * 1000);
    //       var hours = date.getHours();
    //       if(hours>12){hours=hours-12}
    //       var minutes = "0" + date.getMinutes();
    //       var seconds = "0" + date.getSeconds();
    //       var formattedTime = hours + ':' + minutes.substr(-2) + ' ' + 'pm';
    //       sunset.innerHTML = formattedTime;
    //       //sunset.innerHTML = response.sunset;

          

    //       // cloud_pct.innerHTML = response.cloud_pct;
    //       feels_like.innerHTML = response.feels_like;
    //       humidity.innerHTML = response.humidity;
    //       humidity2.innerHTML = response.humidity;
    //       wind_speed.innerHTML = response.wind_speed;
    //       wind_speed2.innerHTML = response.wind_speed;
    //       wind_degrees.innerHTML = response.wind_degrees;
    //     })
    //     .catch((err) => console.error(err));
    // };

    // submit.addEventListener("click", (e) => {
    //   e.preventDefault();
    //   getWeather(input.value);
    // });
    // //api request method end


    // //flask request value start
    // let data1 = document.getElementById("senddata1").innerHTML;
    // getWeather(data1);
    //flask request value end



    document.getElementById("submit_details_page").addEventListener("click",()=>{
      let val=document.querySelector("#input_query_details_page").value;
      document.querySelector("#city_query_details_page").value = val;
      document.forms.city_from.submit();
  })