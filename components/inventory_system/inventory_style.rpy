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
    xsize 600
    ysize 400
    background "components/inventory_system/images/gui/Inventory_frame_BG.png"

style close_btn:
    xpos 550
    ypos 60
    
style inventory_title:
    font "fonts/Jersey25-Regular.otf"
    size 40
    pos (10, -30)
    outlines [(1, "#000000", 0, 0)]
    color Color((222, 222, 222, 255))
style dummy is text:
    size 6

style inventory_container is vbox:
    xpos 170
    ypos 150

style inventory_grid is vpgrid:
    spacing 2
   
style inventory_scrollbar is scrollbar: 
    xsize 1105
    ysize 450
 
style inventory_item_name is text:
    size 11
    bold True
    color Color((255, 255, 255, 255))
    pos (2,0)
 

style inventory_item_quantity is text:
    size 12
    bold True
    color Color((251, 251, 251, 255))
    outlines [(1, "#000000", 0, 0)]
    text_align 1.0
    pos (60, 60)
    xanchor 1.0
    yanchor 1.0
 
style hud_frame is frame:
    xpadding 10
    ypadding 10
    xalign 0.5
    yalign 0.0

style tooltip_text_style is text:
    font "fonts/Quicksand-Medium.ttf"
    size 15
    color "#FFFFFF"
    outlines [(1, "#000000", 0, 0)]
    xalign 0.0
    yalign 0.0
    text_align 0.0
