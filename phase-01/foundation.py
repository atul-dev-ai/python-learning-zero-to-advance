"""
## Folder Create

১০টা folder একসাথে তৈরি:
mkdir -p phase-{01..10}

Specifi
c path এর ভিতরে করতে চাইলে:

mkdir -p mail/phase-{01..10}

---

## Single Folder Create

mkdir phase-01


Nested folder create:
 
mkdir -p project/mail/phase-01

---

## File Create

Empty file:

touch file.txt


একসাথে অনেক file:

touch file-{01..10}.txt

Specific folder এ:

touch phase-01/data.txt

---

## Folder Delete

Empty folder delete:

rmdir phase-01

Folder এর ভিতরে file থাকলেও force delete:

rm -rf phase-01

সব phase folder delete:

rm -rf phase-*


ভুল path দিলে পুরো data উড়ে যাবে। `rm -rf` dangerous command

---

## File Delete

Single file:

rm file.txt

Multiple file:

rm file-*.txt

---

## Rename Folder / File

Folder rename:

mv phase-01 phase-001

File rename:

mv old.txt new.txt

Move + rename একসাথে:

mv file.txt phase-01/newfile.txt

---

## List Files & Folders

ls

Details সহ:

ls -la

---

## Copy

File copy:

cp file.txt backup.txt

Folder copy:

cp -r phase-01 phase-backup

---

## Useful Navigation

Current path:

pwd

Folder change:

cd phase-01

One step back:

cd ..

Home directory:

cd ~

"""