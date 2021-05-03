# Data & Visualization Weekly Projects Report 2021_04_02

## Active Projects 


### Active Development 

* Biosphere 2 Biosystems Visualization Collaboration 
	 * Met with Omani
	 * Started working on the vfx out of unreal engine
	 * There doesn't seem to be many easy ways to control the speed at which some effects propagate
	 * Uploaded Open Root Sim to Jetstream and ran a bunch of sample simulations to give us root meshes to work with
	 * Spent most of my time re-writing the .vtu to .obj script
	 * Facing a really annoying bug in which there's an extra face at the end of each triangle strip, but there's no clues as to how to make sure I'm indexing the correct number of vertices
	 * Once I have this worked out I can send things along to Omani
* Data Visualization Roadshow With Jeff Oliver 
	 * Sent offer for presentation to Dianne Patterson in SLHS
	 * She isn't able to offer actual class time for a presentation
	 * Will have to decide with Jeff if we really don't want to pre-record something for them
	 * Trying the NSCS department next
* Independent Study Abby Collier 
	 * Met with Abby and started working on Touch designer
	 * Wrote a section of Abby's outstanding senior nomination for Rich Thompson who is the primary Python lecturer for ISTA
	 * Worked live through a Touch Designer network showing basic features such as CHOPs TOPs, parameter referencing, and feedback
	 * Then did a very quick intro to programming particle systems as that will be the main thing we generate for the astro dance performance
* Judging The Data Visualization Challenge 
* Migrant Forensic Empathy Project: A Digital Borderlands Grant Initiative 
	 * Got data on lat-lng for migrant deaths along the border from Jonathan
	 * Created simple webmap of this to help understand how many crosses may show up in the Aframe scene
	 * https://mfemigrantdeathmap.baylyd.repl.co/
	 * Unfortunately the previous student has cropped some of the digital elevation map (DEM) from its original bounding box so I can't make a function to map between the lat-lng range in the data and the x-z coordinates  of the landscape model
	 * I had to recreate a Marching Cubes workflow to process the a URL to download a DEM into a 3D mesh
	 * I'll be using the bounding box of this to convert the gps locations of the deaths into positions at which I need to place cross models in the landscape
* Oyster Vibrio Literature Review 
	 * Emily had to reschedule to Tuesday
* Remote Visualization Infrastructure Development 
	 * Created brief statement for Blake to submit to the All hands accomplishments
	 * Met with Chris Reidy to discuss the newest developments
	 * Gave a demo showing the 1.5 million particle attractor using Jetstream Exosphere and the NoMachine remote desktop
	 * Started working on how we can use Vulkan on the HPC
	 * Chris said he would try to install NoMachine on i18n17 so that we can test whether that fixes the `Incompatible Driver` error when running `VulkanInfo`
* Resbaz Organizer And Workshop Provider 
* Stellarscape Astronomy Multimedia Dance Performance 
	 * Rapid prep for presentation of work with our dancer Hayley Meier
	 * Spent the week working on all of our existing visualizations trying to incorporate feedback from Kay


### Consultations 


## Upcoming 

* Bryan Carter Photogrammetry 
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

