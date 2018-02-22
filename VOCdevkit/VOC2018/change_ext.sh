# Rename all *.jpg to *.JPEG
for f in JPEGImages/*.jpg; do
mv -- "$f" "${f%.jpg}.JPEG"
done
