## Search:
   ## self.nextStoneIconChange = 0 
    ## in def __init__(self):  | inside : class InfoBoard(ui.ThinBoard):
    
## Add: 				
        self.itemScrollBar = ui.ScrollBar()
				self.itemScrollBar.Hide()
## search: def Close(self):

## Add :
      self.itemScrollBar.Hide()
## Above self.Hide()

##search: 

							itemScrollBar = ui.ScrollBar()
							itemScrollBar.SetParent(self)
							itemScrollBar.SetPosition(itemListBox.GetRight(), itemListBox.GetTop())
							itemScrollBar.SetScrollBarSize(32 * self.MAX_ITEM_COUNT + 5 * (self.MAX_ITEM_COUNT - 1))
							itemScrollBar.SetMiddleBarSize(float(self.MAX_ITEM_COUNT) / float(height / (32 + 5)))
							itemScrollBar.Show()
							itemListBox.SetScrollBar(itemScrollBar)
## replace it with:


							self.itemScrollBar.SetParent(self)
							self.itemScrollBar.SetPosition(itemListBox.GetRight(), itemListBox.GetTop())
							self.itemScrollBar.SetScrollBarSize(32 * self.MAX_ITEM_COUNT + 5 * (self.MAX_ITEM_COUNT - 1))
							self.itemScrollBar.SetMiddleBarSize(float(self.MAX_ITEM_COUNT) / float(height / (32 + 5)))
							self.itemScrollBar.Show()
							itemListBox.SetScrollBar(self.itemScrollBar)

## that's All Have fun.
