# WATCH
The WATCH (in development) is a simple use item that will provide warmth for cats independently of human intervention.  It was designed to activate when and only when it is actually being used. Upon final implementation, the WATCH should benefit older cats in particular, as they may suffer from arthritis and other joint problems that cause discomfort.
<p>The initial prototype (v01) is a proof-of-concept of the WATCH’s warming and temperature safety functionalities, which are to initiate a warming element to provide comfort via application of weight (use by the cat) and to regulate the surface temperature to an acceptable range.</p>

# Repository Contents
<ul>
  <li><b>Source Code</b><br>The MicroPython source code to be flashed onto the Micro:Bit.</li>
  <li><b>Circuit Diagram</b><br>Fritzing diagram of the project's circuit setup. The diagram is slightly modified from the actual build of the current project, but is labelled for clarity and will be updated with a more accurate setup upon creating custom Fritzing parts for KeyeStudio components. A separate repository for custom Fritzing parts is located <a href="https://github.com/ideocariza/Fritzing-Files.git">here</a>.</li>
</ul>

# Version History
<ul>
  <li>v01 — Initial prototype</li>
 </ul>
 
# Instructions
<h3>v01. Initial Prototype</h3>
<h4>Materials</h4>
<ul>
  <li>Repurposed Boxes</li>
  <ul>
    <li><i>Platform</i><br>5.25”(133.35 mm) W x 6.25”(158.75 mm) L x 1.5”(38.1 mm) H</li>
    <li><i>Base</i><br>3.25”(82.55 mm) W x 6”(152.4 mm) L x 2”(50.8 mm) H</li>
  </ul>
  <li>9V batteries (3)</li>
  <li>9V battery snap wire connectors (3)</li>
  <li>Tool-free wire connectors (2)</li>
  <li>Electrical tape</li>
  <li>Round adhesive foam pads (10mm diameter)</li>
  <li>Female-to-female jumper wire cables (minimum 6; more as needed for length)</li>
  <li>Male-to-female jumper wire cables (as needed for length)</li>
  <li>Double-ended alligator clip jumper wires (2)
  <li>Stranded electrical wire</li>
  <li>BBC Micro:Bit</li>
  <li>1-channel relay module</li>
  <li>Keyestudio Sensor Shield V2.0 for Micro:Bit (ks0360)</li>
  <li>Keyestudio Analog Temperature Sensor (ks0033)</li>
  <li>Keyestudio Thin Film Pressure Sensor (ks0309)</li>
  <li>EeonTex High-Conductivity Heater Fabric</li>
</ul>
<h4>Steps</h4>
<p><b>1. Electrical Hardware and Circuit Construction</b></p>
<p>1.1. Connect the sensor shield to your Micro:Bit.</p>
<p>1.2. Using female-to-female jumper wire cables, connect the 1-channel relay's ground, voltage, and data headers to the respective headers on the sensor shield for pin 13 (or another available digital out pin).</p>
<p>1.3. Using stranded electrical wire, connect the relay module's NO ("normally open" header) to an alligator clip jumper wire. Connect the relay module's COM ("common" pin) to the positive end of a battery wire connector using a stranded electrical wire and a wire connector.</p>
<p>1.4. Connect two more battery wire connectors to the first to create a series of three using wire connectors. Connect the last remaining wire end to an alligator clip jumper wire.</p>
<p>1.5. Connect female-to-female jumper wires into the sensor shield (for appropriate ground, vcc, and data headers) on pin 10 (or another available analog in pin). You will connect these to the temperature sensor in a later step.</p>
<p>1.6. Connect female-to-female jumper wires into the sensor shield as in the previous step to pin 0 (or another analog pin). You will connect these to the pressure sensor in a later step.</p>
<p><b>2. Constructing the Platform and Base Structures</b></p>
<p>2.1. Cut right triangles into diagonally opposite corners of the top of your platform box. The side of the triangles that joins the sides flush with box edges should be 1—1.5 inches across.</p>
<p>2.2. Cut a small circular hole into the center of the top of the platform box lid. Be precise and ensure the location of the center is accurate. Use a straight edge to determine where lines from diagonally opposite corners of the box would intercept if needed.</p>
<p>2.3. On the top of the lid of the base box, cut a hole large enough to run small wires through. Choose a "back" side of the bottom piece of the base box. Cut a hole for wires through this side near the bottom (close to the ground) along this side.</p>
<p>2.4. Mark the center of the interior of the bottom piece of the base box. Do the same for the top outside surface of the top piece of the base box. (Again, be precise. Use a straight edge to determine where lines from diagonally opposite corners of the box would intercept to accomplish this.)</p>
<p>2.5. Cut out a piece of the conductive fabric that is slightly smaller than the platform box lid. Fasten it to the edges of the top of the lid with electrical tape around the perimeter, except for the corners directly near the holes cut in step 2.1.</p>
<p>2.6. Combine adhesive foam pads by layering them on top of one another to a height of about 1". Center this combined foam pad with the mark created on the top outside surface of the top piece of the base box and attach with adhesive backing.<p>
<p><b>3. Combining Hardware</b></p>
<p>3.1. Using electrical tape, attach the pressure sensor to the bottom of the bottom piece of the base box. Make sure that the sensor area is lined up with the center-mark created in the first part of step 2.4. Use as much length of connected jumper cables as needed to finish connecting the sensor to the sensor shield by running them through the hole cut into the back of the base.</p>
<p>3.2. Using electrical tape, attach the temperature sensor to the interior of the platform piece so that the sensor area is slightly bent into the hole cut in step 2.2. Use as much length of connected jumper cables as needed to finish connecting the sensor to the sensor shield by running it through both pieces of the base.</p>
<p>3.3. Fold the respective corners of the conductive fabric into the triangular holes in the platform. Connect the alligator clip from the last battery in the series to one corner by running through the interior of the platform. Do the same with the alligator clip from the relay module to the opposite corner. The fabric itself completes the warming circuit.</p>
<p>3.4. Carefully nest the pieces of the boxes together with the top piece of the base box still upside-down.</p>
<p>3.4. Attach batteries to the battery connectors.</p>
<p><b>4. Code</b></p>
<p>4.1. Flash the <a href="https://github.com/ideocariza/WATCH/blob/master/INFO-697_ideocari_FinalProject.py">provided code</a> to your Micro:Bit.</p>
<p>4.2. Press down on the surface of the platform to judge how sensitive the pressure sensor is. The sensitivity needed depends on the weight of the structure and will vary between builds. Adjust the pressure sensitivity as needed by assigning the pressure a value of an integer no larger than 1024 in your MicroPython code.</p>
<p>4.3. You should notice the relay module switch on when the platform is depressed and switch off when pressure is released. Press down on the platform long enough to test that the circuit and warming function are working. You should feel the conductive fabric change temperature while the circuit closes across it's surface from one alligator clip to the other.<p>

# License Information
This project is licensed under the terms of the MIT license.
