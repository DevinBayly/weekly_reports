# Data & Visualization Weekly Projects Report 2021_04_16

## Active Projects 


### Active Development 

* Advice For Thesis Defense Visualizations, Sabrina Nardin 
	 * Met with Sabrina to discuss her dissertation defense's visualizations
	 * Her data is visualizing 8 different violent events from Italy's history in the last 50 years covered by 3 different newspapers
	 * Most of her questions were about how to improve her existing approaches so I laid out the foundation of "task abstraction" taught to me by Joshua Levine using Tamara Munzner's design theory for visualization
	 * Shared resources with Sabrina and recommended a few changes, but overall tried to equip her with the ability to critique her own work
	 * Mentioned other best practices such as sharing her visualizations with as many other people that are like her target audience as early as possible
* Biosphere 2 Biosystems Visualization Collaboration 
	 * Fixed issues with converting vtu to obj!
	 * Apparently issues stemmed from using 0 based counting in the obj face indices
	 * Gave Omani  full folder of simulation results to work with
	 * Started email chain with Developers at Open Root Sim about how to change the simulation parameters to create different plant root systems
	 * I believe we won't get very far with this because they only focus on a few model plants and nothing bigger than a corn plant
	 * Looked into L systems for generating artificial root structures, but it would be great to get scans of some much bigger plants
	 * Omani started working on the VFX of animating particles traveling along the outsides of the mesh, but I think that's going to take time
* Data Visualization Roadshow With Jeff Oliver 
* Independent Study Abby Collier 
	 * Met up and started working on custom materials
	 * Had long discussion in the meeting cementing  the mental model of how the shaders are using different color channels to move particles
	 * Also started working on how to use other texture inputs to help with particle spreading patterns
	 * Had to rush into using uniform sampler2D types
	 * As a result I made a short video recording explaining how to do modular arithmetic to calculate texture sample coordinates from instance id's  for each of our particles
* Judging The Data Visualization Challenge 
	 * Started reviewing the entries, on track to finish this before the 28th
* Migrant Forensic Empathy Project: A Digital Borderlands Grant Initiative 
	 * Created realistic scaling version, but found that there's visual artifacts on the faces far from the camera, created SO issue for this but I imagine I will just have to downsize the mesh and alter other aspects to make the landscape scale feel appropriate
	 * Spent a while re-writing the cross placement Rust code, so that the quad tree regions feature overlap
	 * This ultimately makes the program less performant but the results are much more accurate
	 * Performance benchmarking by isolating each individual entry of the scene and checking the fps
	 * Learned that there doesn't seem to be any one piece causing performance issues which is comforting
	 * Reached approximately the halfway point of allotted time for this project and there's still some big aspects I still have to implement
* Oyster Vibrio Literature Review 
* Remote Visualization Infrastructure Development 
	 * Met Peter Messmer of Nvidia's HPC remote visualization division at Nvidia GTC
	 * Discussed several projects that I want to leverage their tool Omniverse for
	 * Got positive feedback that streaming results to displays like CATalyst's big display walls or even Biosphere2 should be included in their  Omniverse Beta release that's out now
	 * Met quite a few other individuals who will probably be able to assist with this going forward
	 * Will be testing using Exosphere and my own local machines before looking into HPC -> Catalyst
* Resbaz Organizer And Workshop Provider 
	 * Built workshop Observable notebook
	 * Created observable notebook conversion of Kate Isaac's Vega-lite data visualization workshop
	 * Discussed with Blake what the process would be for adding videos to the resbaz youtube channel, it sounds like he'll take that on just because it sounds like access is a tricky subject
	 * Setup next meeting with Chinmay for following wednesday
* Stellarscape Astronomy Multimedia Dance Performance 
	 * Switched gears in development for this project to curves instead of particle systems
	 * Reviewed videos that Kay sent to me for inspiration
	 * Spent time reading Fundamentals of Computer Graphics chapters on splines, Hermite cubics, and Bezier curves
	 * Made a proof of concept GPU compute touch designer example of 100^2 lines interpolated to a level of detail around 1000 segments per line
	 * Somehow this still ran at 60fps? Not going to argue with the results.
	 * Setup meeting with Gustavo the director of the new Sensor Lab to discuss the sensor options we will have access to for the show
	 * Researched and implemented a system for switching between running Visualizations within Touch Designer so that we can script the whole performance from beginning to end without being hands on
	 * This will be ultimately better because its still pretty likely that we would press the wrong thing at the wrong time and create a technical difficulty


### Consultations 

* Advice For Thesis Defense Visualizations, Sabrina Nardin 

## Upcoming 

* Bryan Carter Photogrammetry 
* Collaboration With Techcore'S Summer Internship 
* Has Faculty Collaborations With Holodeck 
* Jason Hortin Holographic Dance Graduate Project 
* Observablehq Portfolio Of Data Visualization 
* Ray Tracing On The Hpc 


## Completed For Fiscal Year 



### Workshops/Trainings 

* Mt. Lemmon In Your Pocket-Creating A Virtual Reality Tour 
	 * https://rtdatavis.github.io/#GIS_week2020 
* Presentation For Civil Engineering Department 
	 * https://docs.google.com/presentation/d/15Z9zcxU4vIIgFPnKEcaGv9GH7JtjNdx4Xpnjec0EzEc/edit?usp=sharing 
* Tech Core Level Up Presentation Monday, Sept 28 2020 
	 * https://rtdatavis.github.io/#techcoresept28 
* Tech Core Level Up Presentation Tuesday, Mar 17 2020 
	 * https://rtdatavis.github.io/#techcoremar20 
* Womens Hackathon: Visualization On The Web Workshop 
	 * https://womenshackathon.arizona.edu/ 
	 * https://www.youtube.com/channel/UCe1YiJ53o3qcayVs4cipeXA/videos 
	 * https://www.youtube.com/watch?v=VLwPOtqW8oM 


### Completed Projects/Collaborations 

* 3D & Vr Retrofit Azlive 
	 * https://rtdatavis.github.io/#retrofitAZLIVE 
* Bio5 Virtual Reality Tour 
	 * https://rtdatavis.github.io/#bio5-vr-tour 
* Covid Retail Mitigation Web Scraping 
	 * https://rtdatavis.github.io/#retailscraping 
* Force Directed Biochem Networks 
	 * https://rtdatavis.github.io/#biochem-networks 
* Neuro Choropleth 
	 * https://rtdatavis.github.io/#neuro-choro 
* Spring Break Covid Photo Maps 
	 * https://rtdatavis.github.io/#spring-break-covid 


### Infrastructure Developed 

* Autamus Web Interface 
	 * https://rtdatavis.github.io/#autamus_interface 
* Virtualgl For Nvidia Accelerated Remote Hpc Visualizations 
	 * https://rtdatavis.github.io/#virtualgl 
* Xpra And Singularity For Comprehensive Graphical Application Support On Hpc 
	 * https://rtdatavis.github.io/#xprasingularity 


### Protocols and Analysis Developed 

