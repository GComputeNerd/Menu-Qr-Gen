# Menu-Qr-Gen

This is a program which takes a Menu text file, and generates a QR Code for it.

## How to Use

1. Unzip the Menu-QR-Gen.zip file
2. Install python prerequisites using requirements.txt
3. You also need to make sure that you have pdflatex working on your computer.

That's it! You are now all set to use The Generator.

Also for Google Drive Authentication, the Google Drive API is used so you need a OAuth Token for that. Save it as client_secrets.json and you're all set

## Working

This Generator works in 3 steps

1. You provide a Menu Text File. You will see how to write one in the next section. Write the menu and save it with the name format.txt in the same folder as the script. That's all you need to provide. The rest is Automated.
2. The script uses the format.txt file, and generates a LaTeX menu file.
3. The script runs pdflatex and generates a pdf from the LaTeX file.
4. The pdf is then uploaded to your google drive. You do need to authenticate with google drive for this so it will open a browser.
5. The shareable link of the menu pdf from google drive is taken, and a QR code of that link is generated.
6. The QR code is saved as Restaurant-Name-QR_Code.png

Share the QR Code!

The only thing you need to do, is write the Menu, and authenticate with google drive. The rest is all automated.

## Writing a format.txt file

This is how to format a menu in a format.txt file. First of all, start your format.txt with the details in the title page of the menu.

Like so,

```
---
&Logo
=Name: Restaurant Name
=Phone: +00 123 456 789
---
```

If the restaurant has a logo to be included then write `&Logo` and save the logo as logo.png
If the restaurant does not want aa logo delete the `&Logo` line

That is the head of format.txt, below the `---` you have the menu.

```
=Category Name
]item - price
]item - price
!comment
]item - price
--
=Category New Name
]item - price
!comment
--
+
=Specials
]item - price
]item - price
!comment
--
```

The `=Category Name` is how you start a Category write that, and the thing after the `=` Symbol will be the category name.
Inside a Category you can use `]item - price` Replace item with the item, and price with the price. For example like this `]ice cream - 20`
If you would like to say a comment about the ice cream like *A mix of strawberry, blueberry, and coffee* use `!A mix of strawberry, blueberry, and coffee`
Then when you're done with your category Write `--` to show that that's the end of that category.

If in between categories, you would like to have a new page. Use a `+` and it will make a new page.

Once you're done writing the menu, save it in the same folder as this program, under the name format.txt and run the python script.
