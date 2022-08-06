# tla-iot-project
A multi-purpose device that provides the user with updates on home temperature, humidity, air pressure, and altitude. 





<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-econode">About EcoNode</a>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#real-world-applications">Real World Applications</a></li>
    <li><a href="#the-journey">The Journey</a></li>
    <li><a href="#triggers">Triggers</a></li>
    <li><a href="#node-red">Node Red</a></li>
    <li><a href="#python">Python</a></li>
    <li><a href="#photos">Photos</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About EcoNode


EcoNode is an indoor or outdoor air monitoring system, and displays temperature, humidity, air pressure, and altitude values on a easy-to-access dashboard. EcoNode also graphs these values and alerts the user when they are out of their reccomended range. 

For example: If the user is out and left their dog at home, but the temperature rises to 80*F, this could cause their pet to suffocate or become dehydrated! However, EcoNode would have already notified them both physically and verbally, and told them to turn on an air conditioner. The user would recieve the notification, check precise values on their dashboard, and save their pet!

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- GETTING STARTED -->
## Getting Started

Here's a short walkthrough on how to activate EcoNode.



### Installation

1. Run the I2C code in Arduino.

2. Import the json file into Node Red.

3. Go to command prompt and activate Node Red.
   
   ```sh
   node-red
   ```
4. Click on the link given in your command prompt
   ```sh
   http://localhost:1880/
   ```
5. Click "Deploy" and visit the dashboard at http://localhost:1880/ui/
  
   

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Real World Applications

#### A compact system like EcoNode has endless purposes. 

-  Sensing these values in our offices and homes is important, as  humidity and temperature may cause health and structural problems. For example, an indoor temperature less than 55ºF may freeze pipes, and one above 80º can severely damage drywall longterm.

-  EcoNode can be used in industries like paper, textile, food processing, and more, since they need to regulate specific humidities and temperatures

-  Some irrigation techniques needs precise humidity for plants. The moisture present in the soil also plays an important role. Moreover, indoor vegetation also requires humidity sensors.

-  Many electronic devices are graded with a range of humidity values. Generally, this value is between 10 to 50% humidity. Semiconductor fabrication plants need to maintain very accurate humidity and temperature values, as even a difference of a minute can hugely impact the production.

-  Medical equipment like sterilizers and incubators also need temp and humidity control. Exact values are used in biological processes and pharmaceutical plants as well.



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- The Journey -->
## The Journey

- Last summer, I had the oppurtunity to participate in this program, and use the DHT22 sensor and a light sensor resistor to build a very cool device. This year, though creativity was limited, I was very excited to test out the BME688's gas sensing capabilities. 

- However, I faced many difficulties, the first being that my BME688's gas resistance didn't change at all.
 - After many failed attempts to change the gas resistance, including coffee, shampoo, hydrogen peroxide, and paint out-gassing, I decided to use what I had and base my project on the values that worked: Temperature, Humidity, Air Pressure, and ALtitude.
- Not too long after that, my ESP32 Thing Plus board stopped working, and I ended up using the RedBoard instead, despite the fact that it couldn't connect wirelessly.
- I struggled a lot with getting the plotting code in Python to work as well, but with a few days of online forums and youtube, I finally solved the issue. 
 - I learned a lot more about syntax in Python, C++, and Javascipt, since they were all used in my project. I used to be sightly afraid of programming, since it appeared very complicated. After having to debug so much code myself this summer, I am much more confident in my abilities.
- Lastly, since I couldn't put my data on a webpage easily without an ESP32 board, I searched for a local option. After trying various other dashboards, Node Red finally worked for me. 
 - Node Red was probably the part of my project that took the most debugging, but I learned the most from it. And now I have a working dashboard that displays my data and keeps values in check!
    

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Triggers -->
## Triggers

When the temperature goes above 82º F, Node Red will send you a notification and verbally state that the temperature is too high.

The same thing applies for low temperature (x < 60º), high humidity (x > 50%), low humidity (x < 30%), and low/high air pressure (x < 970 hPa or x > 1030 hPa)


<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTRIBUTING -->
## Node Red

Node Red handles all sensor data, and outputs it onto a dashboard. 

The code for my flow can be found in the repository. To try it out, simply download Node Red on your command prompt, and go to the link it gives you. Then go to:

Menu -> Import -> Paste the json file there

You should see something like this:

![Screen Shot 2022-08-05 at 9 24 13 PM](https://user-images.githubusercontent.com/100453801/183228303-4eb4dcea-2a84-4f93-9816-67be6a860189.png)

As you can see, my setup first seperates serial data values, converts temperature to Fahrenheit, then puts all these values on the dashboard. It also graphs these values, and reguarly checks if they are in the reccomended range. If they are not, it will notify the user physically and verbally with the Text to Speech nodes.

Below you can see how simple it is to activate the node red local connection. Just a simple line in your command prompt and you can view the dashboard.

![node red gif](https://user-images.githubusercontent.com/100453801/183228548-41d2b6c0-2a02-4ea2-9bc4-5623bbec6aba.gif)

Here's a view of what the dashboard looks like:

![node red graphed data gif](https://user-images.githubusercontent.com/100453801/183228793-77b2b052-9ea4-4d2d-b573-134575e46a04.gif)

Data is stored for an hour, then is replaced by new incoming data. All lines from the serial monitor are also saved in a file on the local Desktop with a timestamp.

Here is the second page of the dashboard:

![node red readings gif hot temp](https://user-images.githubusercontent.com/100453801/183228827-788f4dab-4802-498d-b68d-1956850bfd89.gif)
 
 This gif shows the values' reading changing when I exposed it to humid and hot air. This triggered the notification and Text-to-Speech node as well, shown in the following video.
 
https://user-images.githubusercontent.com/100453801/183229025-45d44e53-2cea-469c-9e94-1595925a781a.mov

In summary, the user will be notified if temperature, humidity, or air pressure values go out of its reccomended range.

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- Python -->
## Python

Lastly, if plotter.py is run while serial data is incoming, MatPlotLib will plot these values and label them. Although, Node Red is reccomended for this system.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Ria Saheta: riasaheta@gmail.com

Project Link: [https://github.com/peanutz28/tla-iot-project](https://github.com/peanutz28/tla-iot-project)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Photos -->
## Photos and Videos

Here's a picture of my set up:

![IMG_3189-removebg-preview](https://user-images.githubusercontent.com/100453801/183230374-13ebafa3-b1d5-49a0-b84e-32325087e764.png)

Below is a video of one of my failed gas resistance tests, using the out-gassing from paint.


https://user-images.githubusercontent.com/100453801/183230471-967a06a4-a3ad-46a7-8cc7-af4b771ad9e7.mov



https://user-images.githubusercontent.com/100453801/183231026-75e94a8a-f340-4f25-8c73-6eb202fe53f9.mov




<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
