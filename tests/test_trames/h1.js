// const url = 'https://climate-news27.p.rapidapi.com/news';
// const options = {
// 	method: 'GET',
// 	headers: {
// 		'X-RapidAPI-Key': 'ea77a70441msh0f1a928a9888502p13bdbbjsncaf20ee225b5',
// 		'X-RapidAPI-Host': 'climate-news27.p.rapidapi.com'
// 	}
// };

// try {
// 	const response = fetch(url, options);
// 	const result = response.text();
// 	console.log(result);
// } catch (error) {
// 	console.error(error);
// }



const options = {
    method: "GET",
    headers: {
      "X-RapidAPI-Key": "ea77a70441msh0f1a928a9888502p13bdbbjsncaf20ee225b5",
      "X-RapidAPI-Host": "climate-news27.p.rapidapi.com",
    }
  };
  
const getWeather = () => {
fetch("https://climate-news27.p.rapidapi.com/news", options)
    .then((response) => response.json())
    .then((response) => {
    console.log(response);
    })
    .catch((err) => console.error(err));
};