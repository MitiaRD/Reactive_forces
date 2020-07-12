# Reactive_forces
Python script to calculate reactive forces on a beam based on the simplified 'method of sections' method in Solid Body Mechanics.

The solid body mechanics 'method by sections' is a method of calculating forces in trusses and beams, this program is the initial stage in the method which simply aims to 
calculate the reactive forces that a single beam experiences once a force is applied. Essentially we can imagine our beam to be a simplified "bridge" and our aim is to calculate
the forces exerted on the bridges contact points (e.i the ground). 

This is simply calculated by initially 'breaking' the beam at the point of applied force and calculating the moment about one connection point (moment = force * distance) 
upon calculating this we can then determine the reaction forces in either contact point.
