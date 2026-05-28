"""
EST 4 Pricing Data — NYC Commercial Interior Construction
Base rates derived from Vornado Renaissance 44F project (1,233 SF TI).
All rates in USD. Low/High represent NYC union labor market range.
"""

DIVISIONS = {
    "01": {
        "name": "General Conditions & Requirements",
        "items": [
            {"code": "01.01", "description": "GC Project Management & Superintendent", "uom": "WKS", "unit_low": 4500, "unit_high": 6000},
            {"code": "01.02", "description": "Building Protection (elevator pads, lobby/corridor)", "uom": "LS", "unit_low": 4000, "unit_high": 6000},
            {"code": "01.03", "description": "High-Floor Hoisting & Material Logistics Premium", "uom": "LS", "unit_low": 5000, "unit_high": 8000},
            {"code": "01.04", "description": "Temporary Facilities (lighting, power, safety)", "uom": "LS", "unit_low": 2000, "unit_high": 3000},
            {"code": "01.05", "description": "Temporary Construction Partitions / Dust Barriers", "uom": "LS", "unit_low": 2500, "unit_high": 4000},
            {"code": "01.06", "description": "Debris Removal & Dumpster / Hoist Fees", "uom": "LS", "unit_low": 6000, "unit_high": 9000},
            {"code": "01.07", "description": "Final Cleaning (project area + common areas)", "uom": "LS", "unit_low": 2500, "unit_high": 3500},
            {"code": "01.08", "description": "Insurance, Bonds & Permits", "uom": "LS", "unit_low": 5000, "unit_high": 7000},
            {"code": "01.09", "description": "As-Built Drawings & Closeout Documentation", "uom": "LS", "unit_low": 1500, "unit_high": 2500},
            {"code": "01.10", "description": "NYC Building Dept. Site Safety Compliance", "uom": "LS", "unit_low": 2000, "unit_high": 3500},
            {"code": "01.11", "description": "Attic Stock Allowance (10% carpet, ACT, wallcovering)", "uom": "LS", "unit_low": 2000, "unit_high": 3000},
        ]
    },
    "02": {
        "name": "Demolition & Site Preparation",
        "items": [
            {"code": "02.01", "description": "Selective Demo – partition walls (patch & repair)", "uom": "LS", "unit_low": 5000, "unit_high": 7000},
            {"code": "02.02", "description": "Remove existing doors, frames & hardware", "uom": "EA", "unit_low": 350, "unit_high": 500},
            {"code": "02.03", "description": "Grind/flash concrete floor for new partitions", "uom": "SF", "unit_low": 2.5, "unit_high": 4},
            {"code": "02.04", "description": "Cap & conceal abandoned piping", "uom": "LS", "unit_low": 2000, "unit_high": 3500},
            {"code": "02.05", "description": "Remove existing convector covers", "uom": "EA", "unit_low": 300, "unit_high": 450},
            {"code": "02.06", "description": "Protect existing columns w/ fireproofing", "uom": "LS", "unit_low": 1500, "unit_high": 2500},
            {"code": "02.07", "description": "Patch & repair existing walls for new finish", "uom": "SF", "unit_low": 4, "unit_high": 7},
            {"code": "02.08", "description": "Remove existing ceiling grid/tile in demo areas", "uom": "SF", "unit_low": 2, "unit_high": 3.5},
            {"code": "02.09", "description": "Demo flooring (existing tile, adhesive)", "uom": "SF", "unit_low": 1.5, "unit_high": 2.5},
            {"code": "02.10", "description": "General demolition debris haul-away", "uom": "LS", "unit_low": 3000, "unit_high": 5000},
        ]
    },
    "03": {
        "name": "Concrete / Floor Preparation",
        "items": [
            {"code": "03.01", "description": "Diamond-polish existing slab to 1500 grit", "uom": "SF", "unit_low": 10, "unit_high": 16},
            {"code": "03.02", "description": "Lithium-based concrete densifier application", "uom": "SF", "unit_low": 1.5, "unit_high": 2.5},
            {"code": "03.03", "description": "Self-leveling underlayment – transition/leveling areas", "uom": "SF", "unit_low": 3, "unit_high": 5},
            {"code": "03.04", "description": "Fill & patch abandoned core holes (rated)", "uom": "EA", "unit_low": 300, "unit_high": 500},
            {"code": "03.05", "description": "Floor surface prep (scarify/clean) prior to finish", "uom": "SF", "unit_low": 0.75, "unit_high": 1.25},
        ]
    },
    "05": {
        "name": "Metals – Column Fireproofing Repair",
        "items": [
            {"code": "05.01", "description": "Repair/patch spray fireproofing on existing columns", "uom": "LS", "unit_low": 2000, "unit_high": 3500},
            {"code": "05.02", "description": "Extend column GYP.BD. enclosures to deck", "uom": "LF", "unit_low": 45, "unit_high": 70},
        ]
    },
    "06": {
        "name": "Millwork, Casework & Appliances",
        "items": [
            {"code": "06.01", "description": "ADA sink base cabinet w/ toe kick", "uom": "EA", "unit_low": 3200, "unit_high": 4500},
            {"code": "06.02", "description": "Trash/recycle pullout base cabinet", "uom": "EA", "unit_low": 1800, "unit_high": 2800},
            {"code": "06.03", "description": "Microwave drawer base cabinet", "uom": "EA", "unit_low": 2000, "unit_high": 2800},
            {"code": "06.04", "description": "Standard base cabinet (3-drawer)", "uom": "EA", "unit_low": 1800, "unit_high": 2600},
            {"code": "06.05", "description": "Upper cabinets (AWI Premium Grade)", "uom": "LF", "unit_low": 650, "unit_high": 900},
            {"code": "06.06", "description": "Full-height panel-ready refrigerator enclosure", "uom": "EA", "unit_low": 2200, "unit_high": 3200},
            {"code": "06.07", "description": "Quartz countertop (2CM)", "uom": "SF", "unit_low": 95, "unit_high": 135},
            {"code": "06.08", "description": "Ceramic tile backsplash (supply & install)", "uom": "SF", "unit_low": 28, "unit_high": 42},
            {"code": "06.09", "description": "Laminate accent panels", "uom": "SF", "unit_low": 18, "unit_high": 28},
            {"code": "06.10", "description": "Floating shelves w/ hardware (private office)", "uom": "LS", "unit_low": 2200, "unit_high": 3500},
            {"code": "06.11", "description": "Coat closet – rod, shelf, apron & blocking", "uom": "EA", "unit_low": 800, "unit_high": 1400},
            {"code": "06.12", "description": "IT closet – FR plywood backboard", "uom": "SF", "unit_low": 18, "unit_high": 28},
            {"code": "06.13", "description": "FR blocking (TV, cabinet mounting throughout)", "uom": "LS", "unit_low": 1500, "unit_high": 2500},
            {"code": "06.14", "description": "Millwork hardware allowance", "uom": "LS", "unit_low": 2500, "unit_high": 3800},
            {"code": "06A.01", "description": "Built-In Refrigerator (supply & install)", "uom": "EA", "unit_low": 7200, "unit_high": 8800},
            {"code": "06A.02", "description": "Built-In Microwave Drawer (supply & install)", "uom": "EA", "unit_low": 700, "unit_high": 900},
        ]
    },
    "07": {
        "name": "Thermal, Moisture & Firestopping",
        "items": [
            {"code": "07.01", "description": "Firestopping at rated wall/floor penetrations (ASTM E-814)", "uom": "LS", "unit_low": 3500, "unit_high": 5500},
            {"code": "07.02", "description": "Top-of-wall firestopping at non-deck partitions", "uom": "LF", "unit_low": 10, "unit_high": 16},
            {"code": "07.03", "description": "Acoustic sealant at all partition joints (both sides)", "uom": "LF", "unit_low": 3, "unit_high": 5},
            {"code": "07.04", "description": "Sound attenuation batt insulation in partitions", "uom": "SF", "unit_low": 1.5, "unit_high": 2.5},
            {"code": "07.05", "description": "Pillow insulation in convectors below demising partitions", "uom": "EA", "unit_low": 150, "unit_high": 250},
        ]
    },
    "08": {
        "name": "Openings – Doors, Frames, Hardware & Glazing",
        "items": [
            {"code": "08.01", "description": "Framed glass entry door w/ sidelite (3'x8'4\")", "uom": "EA", "unit_low": 6500, "unit_high": 9500},
            {"code": "08.02", "description": "Glass entry door hardware set (mag lock, closer, pivot)", "uom": "LS", "unit_low": 4500, "unit_high": 6500},
            {"code": "08.03", "description": "HM frame & HM door (interior, 3'x7'10\")", "uom": "EA", "unit_low": 1800, "unit_high": 2600},
            {"code": "08.04", "description": "Interior door hardware set (lever, hinges, closer)", "uom": "LS", "unit_low": 700, "unit_high": 1100},
            {"code": "08.05", "description": "Wood frameless double door (2-leaf)", "uom": "EA", "unit_low": 2800, "unit_high": 4200},
            {"code": "08.06", "description": "Closet door hardware set (pivot, catch, stop)", "uom": "LS", "unit_low": 500, "unit_high": 850},
            {"code": "08.07", "description": "Card reader backbox & conduit infrastructure", "uom": "EA", "unit_low": 800, "unit_high": 1200},
            {"code": "08.08", "description": "Demountable Glass Wall System (KI Lightline or equal)", "uom": "SF", "unit_low": 160, "unit_high": 220},
            {"code": "08.09", "description": "Framed Glass Partition (1/2\" tempered butt joint)", "uom": "SF", "unit_low": 130, "unit_high": 175},
            {"code": "08.10", "description": "Window shades w/ aluminum pocket (ceiling-mount)", "uom": "EA", "unit_low": 2200, "unit_high": 3500},
            {"code": "08.11", "description": "Distraction film (safety marker, per spec)", "uom": "SF", "unit_low": 18, "unit_high": 28},
        ]
    },
    "09": {
        "name": "Finishes – Framing, Drywall, Ceilings, Flooring, Paint, Wallcovering",
        "items": [
            {"code": "09.01", "description": "Partition – 3-5/8\" MS, 1HR UL rated, to deck w/ sound batt", "uom": "LF", "unit_low": 85, "unit_high": 120},
            {"code": "09.02", "description": "Partition – 6\" MS, 1HR rated, to deck w/ insulation", "uom": "LF", "unit_low": 90, "unit_high": 130},
            {"code": "09.03", "description": "Partition – 2-1/2\" MS, non-rated, sound batt both sides, to deck", "uom": "LF", "unit_low": 65, "unit_high": 95},
            {"code": "09.04", "description": "Partition – 3-5/8\" MS, non-rated, sound batt both sides, to ceiling", "uom": "LF", "unit_low": 55, "unit_high": 80},
            {"code": "09.05", "description": "Partition – 2-1/2\" MS, single side, to deck", "uom": "LF", "unit_low": 45, "unit_high": 65},
            {"code": "09.06", "description": "Partition – 3-5/8\" MS, non-rated, both sides, to ceiling (col. enclosures)", "uom": "LF", "unit_low": 50, "unit_high": 75},
            {"code": "09.07", "description": "GYP.BD. soffit header at demountable wall", "uom": "LF", "unit_low": 75, "unit_high": 110},
            {"code": "09.08", "description": "Blocking, backing & bracing – all framed partitions", "uom": "LS", "unit_low": 3500, "unit_high": 5500},
            {"code": "09.09", "description": "Corner bead, tape, 3-coat finish – Level 4/5", "uom": "SF", "unit_low": 2.5, "unit_high": 3.5},
            {"code": "09.10", "description": "ACT – Armstrong Optima 4'x4' sq. tegular w/ Suprafine grid", "uom": "SF", "unit_low": 9, "unit_high": 13},
            {"code": "09.11", "description": "ACT – Armstrong Optima 2'x6' sq. tegular (meeting room)", "uom": "SF", "unit_low": 9, "unit_high": 13},
            {"code": "09.12", "description": "ACT – Armstrong Optima 2'x2' sq. tegular (BOH/utility)", "uom": "SF", "unit_low": 9, "unit_high": 13},
            {"code": "09.13", "description": "Shadow molding perimeter (ACT ceiling areas)", "uom": "LF", "unit_low": 12, "unit_high": 18},
            {"code": "09.14", "description": "GYP.BD. ceiling (5/8\" sag-resistant)", "uom": "SF", "unit_low": 14, "unit_high": 20},
            {"code": "09.15", "description": "GYP.BD. ceiling soffits & return air soffits", "uom": "SF", "unit_low": 16, "unit_high": 24},
            {"code": "09.16", "description": "K-13 acoustic spray – open/exposed deck & beams", "uom": "SF", "unit_low": 5, "unit_high": 8},
            {"code": "09.17", "description": "PVC fittings on high-pressure convector ductwork", "uom": "EA", "unit_low": 85, "unit_high": 140},
            {"code": "09.18", "description": "Ceiling access panels (Stealth Panel or equal)", "uom": "EA", "unit_low": 250, "unit_high": 400},
            {"code": "09.19", "description": "Carpet tile (24\"x24\" vertical ashlar)", "uom": "SF", "unit_low": 8.5, "unit_high": 12},
            {"code": "09.20", "description": "Polished concrete – grind, polish, densifier (see Div 03)", "uom": "SF", "unit_low": 0, "unit_high": 0},
            {"code": "09.21", "description": "Static dissipative tile (IT closet)", "uom": "SF", "unit_low": 9, "unit_high": 14},
            {"code": "09.22", "description": "Transition strip – concrete to carpet (Schluter or equal)", "uom": "LF", "unit_low": 28, "unit_high": 42},
            {"code": "09.23", "description": "Transition strip – concrete to resilient", "uom": "LF", "unit_low": 22, "unit_high": 35},
            {"code": "09.24", "description": "Rubber base 4-1/4\"H", "uom": "LF", "unit_low": 4, "unit_high": 6},
            {"code": "09.25", "description": "Paint – 1 primer + 2 coats eggshell on walls", "uom": "SF", "unit_low": 2, "unit_high": 3},
            {"code": "09.26", "description": "Paint – flat on ceilings; semi-gloss on doors/frames", "uom": "SF", "unit_low": 2, "unit_high": 3},
            {"code": "09.27", "description": "Paint – exposed structure, conduit, ductwork (open ceiling)", "uom": "SF", "unit_low": 1.5, "unit_high": 2.5},
            {"code": "09.28", "description": "Wallcovering – accent wall (meeting room)", "uom": "SF", "unit_low": 22, "unit_high": 32},
            {"code": "09.29", "description": "Wallcovering – accent walls (private offices)", "uom": "SF", "unit_low": 25, "unit_high": 38},
            {"code": "09.30", "description": "Wallcovering – specialty accent location", "uom": "SF", "unit_low": 28, "unit_high": 42},
            {"code": "09.31", "description": "Convector cover replacement – 14GA steel, per spec", "uom": "LF", "unit_low": 300, "unit_high": 480},
            {"code": "09.32", "description": "Recessed fire extinguisher cabinet (tempered glass)", "uom": "EA", "unit_low": 1800, "unit_high": 2600},
        ]
    },
    "10": {
        "name": "Specialties",
        "items": [
            {"code": "10.01", "description": "Accessibility signage – room ID, wayfinding (ADA)", "uom": "LS", "unit_low": 1500, "unit_high": 2500},
            {"code": "10.02", "description": "Fire extinguisher (2-A:10B:C rated)", "uom": "EA", "unit_low": 150, "unit_high": 250},
            {"code": "10.03", "description": "Coat hooks per door schedule (ADA height)", "uom": "EA", "unit_low": 85, "unit_high": 150},
        ]
    },
    "22": {
        "name": "Plumbing",
        "items": [
            {"code": "22.01", "description": "Faucet supply & install (single-hole, gooseneck)", "uom": "EA", "unit_low": 850, "unit_high": 1200},
            {"code": "22.02", "description": "Undermount sink supply & install", "uom": "EA", "unit_low": 600, "unit_high": 900},
            {"code": "22.03", "description": "New domestic water supply + drain rough-in (copper/PVC)", "uom": "LS", "unit_low": 5500, "unit_high": 9000},
            {"code": "22.04", "description": "ADA under-sink insulation cover", "uom": "EA", "unit_low": 250, "unit_high": 400},
            {"code": "22.05", "description": "Above-counter water line stub-out (coffee/appliance)", "uom": "EA", "unit_low": 900, "unit_high": 1500},
            {"code": "22.06", "description": "Plumbing coordination with MEP engineer drawings", "uom": "LS", "unit_low": 1500, "unit_high": 2500},
            {"code": "22.07", "description": "Pressure testing, inspections & NYC plumbing sign-off", "uom": "LS", "unit_low": 2000, "unit_high": 3500},
        ]
    },
    "23": {
        "name": "Mechanical / HVAC",
        "items": [
            {"code": "23.01", "description": "Relocate/rebalance supply diffusers (per new RCP)", "uom": "EA", "unit_low": 650, "unit_high": 1000},
            {"code": "23.02", "description": "Relocate return air grilles / linear returns per RCP", "uom": "EA", "unit_low": 550, "unit_high": 850},
            {"code": "23.03", "description": "Occupancy/vacancy sensor coordination & mounting", "uom": "EA", "unit_low": 350, "unit_high": 550},
            {"code": "23.04", "description": "Window shade pocket integration w/ convector cover", "uom": "EA", "unit_low": 250, "unit_high": 400},
            {"code": "23.05", "description": "Return air opening at slab-to-deck partitions", "uom": "EA", "unit_low": 200, "unit_high": 350},
            {"code": "23.06", "description": "VAV box accessibility verification & relocation (if req'd)", "uom": "LS", "unit_low": 1500, "unit_high": 3000},
            {"code": "23.07", "description": "MEP coordination drawings & above-ceiling coordination", "uom": "LS", "unit_low": 2000, "unit_high": 3500},
        ]
    },
    "26": {
        "name": "Electrical",
        "items": [
            {"code": "26.01", "description": "Devices – duplex/quad receptacles, data/tel boxes", "uom": "EA", "unit_low": 280, "unit_high": 420},
            {"code": "26.02", "description": "Poke-through for workstation power & data conduits", "uom": "EA", "unit_low": 600, "unit_high": 950},
            {"code": "26.03", "description": "Under-cabinet lighting circuit & wiring", "uom": "EA", "unit_low": 450, "unit_high": 700},
            {"code": "26.04", "description": "Downlight (gypsum housing) – rough-in, circuit & trim", "uom": "EA", "unit_low": 300, "unit_high": 450},
            {"code": "26.05", "description": "Downlight (ACT housing) – rough-in, circuit & trim", "uom": "EA", "unit_low": 280, "unit_high": 420},
            {"code": "26.06", "description": "Pendant fixture – rough-in, circuit & hang (large)", "uom": "EA", "unit_low": 450, "unit_high": 700},
            {"code": "26.07", "description": "Pendant fixture – rough-in, circuit & hang (standard)", "uom": "EA", "unit_low": 400, "unit_high": 600},
            {"code": "26.08", "description": "Recessed fixture (4\" & 6\") – rough-in, circuit & trim", "uom": "EA", "unit_low": 300, "unit_high": 450},
            {"code": "26.09", "description": "Architectural linear fixture (utility/closet)", "uom": "EA", "unit_low": 350, "unit_high": 550},
            {"code": "26.10", "description": "Exit signs – emergency power circuit (2 locations)", "uom": "EA", "unit_low": 500, "unit_high": 750},
            {"code": "26.11", "description": "Conduit & backbox for mag lock + power supply wiring", "uom": "LS", "unit_low": 1200, "unit_high": 1900},
            {"code": "26.12", "description": "Card reader conduit & backbox infrastructure", "uom": "EA", "unit_low": 700, "unit_high": 1100},
            {"code": "26.13", "description": "Hard conduit for devices in open ceiling area", "uom": "LS", "unit_low": 3500, "unit_high": 5500},
            {"code": "26.14", "description": "Appliance circuits (refrigerator, microwave, etc.)", "uom": "EA", "unit_low": 450, "unit_high": 700},
            {"code": "26.15", "description": "Panelboard circuit additions / breakers for new loads", "uom": "LS", "unit_low": 2000, "unit_high": 3500},
            {"code": "26.16", "description": "FR plywood backboard, painted white (IT closet)", "uom": "EA", "unit_low": 350, "unit_high": 550},
            {"code": "26.17", "description": "Testing, commissioning & NYC electrical inspection", "uom": "LS", "unit_low": 1500, "unit_high": 2500},
        ]
    },
    "28": {
        "name": "Fire Protection – Sprinkler System Modifications",
        "items": [
            {"code": "28.01", "description": "Sprinkler head relocations (per new ceiling/partition layout)", "uom": "EA", "unit_low": 550, "unit_high": 900},
            {"code": "28.02", "description": "Sprinkler branch line modifications as required", "uom": "LS", "unit_low": 2000, "unit_high": 3500},
            {"code": "28.03", "description": "Sprinkler permit / NYC FD submission and approval", "uom": "LS", "unit_low": 1500, "unit_high": 2500},
            {"code": "28.04", "description": "Inspections, testing & FD sign-off", "uom": "LS", "unit_low": 1000, "unit_high": 1800},
        ]
    },
}

GC_OVERHEAD_PROFIT_PCT = 0.12   # 12%
CONTINGENCY_PCT = 0.05           # 5%

STANDARD_EXCLUSIONS = [
    "MEP engineering drawings – subcontractor quotes required",
    "Furniture, fixtures & equipment (FF&E) – Owner furnished unless noted",
    "IT/AV/Security cabling and terminations – by specialty subcontractor",
    "Permit fees, DOB filing fees, special inspection fees",
    "NYC prevailing wage / union labor requirements assumed throughout",
    "Asbestos survey and abatement (if required prior to demolition)",
    "Architect / engineering fees",
    "Building management fees (overtime HVAC, hoisting charges) – to be confirmed",
    "Low-voltage, fire alarm devices – by Owner's vendors; GC provides conduit/backboxes only",
    "Any work above ceiling or below slab",
]
