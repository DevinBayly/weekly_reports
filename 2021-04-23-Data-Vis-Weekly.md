# Data & Visualization Weekly Projects Report 2021_04_23

## Active Projects 


### Active Development 

* Advice For Thesis Defense Visualizations, Sabrina Nardin 
	 * Met with Sabrina to discuss her dissertation defense's visualizations
	 * Her data is visualizing 8 different violent events from Italy's history in the last 50 years covered by 3 different newspapers
	 * Most of her questions were about how to improve her existing approaches so I laid out the foundation of "task abstraction" taught to me by Joshua Levine using Tamara Munzner's design theory for visualization
	 * Shared resources with Sabrina and recommended a few changes, but overall tried to equip her with the ability to critique her own work
	 * Mentioned other best practices such as sharing her visualizations with as many other people that are like her target audience as early as possible
	 * Has asked for a follow up based on changes incorporated since the meeting
* Biosphere 2 Biosystems Visualization Collaboration 
	 * Met with Omani, and started in a new direction
	 * We will base our work on her photo realistic nature scene
	 * Take models from it and convert into the 2 types of assets that I've identified in the tree-hugger video (pseudo lidar, dynamic point paths)
	 * She asked to specifically learn more about shaders so I've started teaching that material using the shadertoy program, I should mention to her that touch is free for non commercial and perhaps it will run on her laptop
	 * I have to decide what makes sense to do with the results that I already have from the Open Root Sim if we go in this direction
	 * Ash Black was interested in this project in our meeting, perhaps find a way to make this into work that his students can take on
* Data Visualization Roadshow With Jeff Oliver 
	 * Heard back from the NSCS department about a presentation
	 * Just working on the date for the presentation
	 * Presenting to undergraduates also
* Independent Study Abby Collier 
	 * Had our usual friday meeting
	 * Made quite a bit of progress on her feature Touch Designer piece called "purple stars"
	 * Spent time working on her github webpage to present the work from this independent study
	 * Talked about potential for her to continue in this capacity after graduation as a DCC
* Judging The Data Visualization Challenge 
	 * Two more entries of 15 to judge, had a few issues with the rubric in the process
	 * Likely will circle back just to make sure I'm executing my judging process consistently on some of the more nuanced scoring categories
* Migrant Forensic Empathy Project: A Digital Borderlands Grant Initiative 
	 * Got answers about the visual artifacts on SO, sounds like it is a camera parameter issue, hopefully I can still resolve it using a shadeless environment texture
	 * Re-implemented the quad tree algorithm to allow for subsection overlap, unfortunately this caused my recursive algorithm to stack overflow when I put greater limits on the number of elements per region
	 * Re-learned some more advanced methods in rust that will allow me to write the "populate quadtree" and "query" algorithms without recursion
	 * For the mean time, just started long running task and processed cross placements much more accurately
	 * It's pretty heartbreaking to see the crosses that are right next to each other  https://test-cross-placement.baylyd.repl.co/
* Oyster Vibrio Literature Review 
* Remote Visualization Infrastructure Development 
	 * Chris notified me that NoMachine was installed on i18n16, but there's firewall issues with port 4000 so I wasn't able to test this out
	 * Met other members of the Omniverse team who are willing to help me when I run into issues with remote visualization for my projects
	 * Tangentially related, I figured out how to render raw byte streams of data over TCP in the Touch Designer program which may be a personal method for doing remote visualization from simulations running on the HPC
* Resbaz Organizer And Workshop Provider 
	 * Met Chinmay and we discussed some final todo items
	 * Testing our links next week and publishing them to the website team
	 * Noticed that my workshop still isn't listed on the resbaz page so I'll have to get in touch with Alex about that
	 * Blake volunteered to perform the uploads to youtube so that's helpful, still haven't heard from Kelsey about whether our unlisted approach is going to be the correct way to go
* Stellarscape Astronomy Multimedia Dance Performance 
	 * Worked out how to use the Engine COMP to start processes in other threads so that we can keep our visualization performance high
	 * This enabled me to implement a TCP client that receives raw bytes and converts them to a texture that we can operate on with the GPU
	 * I believe this will help me bring the HPC into the project in bigger ways
	 * Spent more time learning how to create multi segment lines in the compute shader


### Consultations 

* Advice For Thesis Defense Visualizations, Sabrina Nardin 

## Upcoming 

* Bryan Carter Photogrammetry 
* Collaboration With Techcore's Summer Internship 
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

