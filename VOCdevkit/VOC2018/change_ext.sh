# Rename all *.JPEG to *.jpg
for f in JPEGImages/*.JPEG; do
mv -- "$f" "${f%.JPEG}.jpg"
done
