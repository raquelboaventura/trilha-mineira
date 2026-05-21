# close icon 
image close:
    "components/inventory_system/images/gui/close.png"
    size(30,30) 
    
image close_hover:
    "components/inventory_system/images/gui/close_hover.png"
    size(30,30) 

style inventory_frame is frame:
    xalign 0.5
    yalign 0.3
    xsize 1000
    ysize 724
    background "components/inventory_system/images/gui/Inventory_frame_BG.png"

style close_btn:
    xpos 675
    ypos 140
    
style inventory_title:
    font "fonts/Jersey25-Regular.otf"
    size 40
    xalign 0.5
    ypos -35
    outlines [(1, "#000000", 0, 0)]
    color Color((222, 222, 222, 255))
style dummy is text:
    size 6

style inventory_container is vbox:
    xpos 305
    ypos 210
    xsize 390

style inventory_grid is vpgrid:
    spacing 15
   
style inventory_scrollbar is scrollbar: 
    xsize 1105
    ysize 450
 
style inventory_item_name is text:
    size 10
    bold True
    color Color((255, 255, 255, 255))
    xalign 0.5
    ypos 8
    text_align 0.5
    outlines [(1, "#000000", 0, 0)]
 

style inventory_item_quantity is text:
    size 12
    bold True
    color Color((251, 251, 251, 255))
    outlines [(1, "#000000", 0, 0)]
    xalign 0.9
    yalign 0.9
 
style hud_frame is frame:
    xpadding 10
    ypadding 10
    xalign 0.5
    yalign 0.0

style tooltip_text_style is text:
    font "fonts/Quicksand-Medium.ttf"
    size 22
    color "#FFFFFF"
    outlines [(1, "#000000", 0, 0)]
    xalign 0.0
    yalign 0.0
    text_align 0.0
