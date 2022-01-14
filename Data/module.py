{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c812a517-a782-4638-bcbb-7eee8c8cf4f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def gene_names(gene_file,gene_names)\n",
    "    with open(gene_file, 'r') as myfile:\n",
    "        with open(gene_names, 'w') as myfile2:\n",
    "            file=myfile.readlines()\n",
    "            #print(file)\n",
    "            for x,line in enumerate(file):\n",
    "                #print(x,line)\n",
    "                if x > 35:\n",
    "                    split_lines=line.split()\n",
    "                    column=split_lines[0]\n",
    "                    if column.startswith('-'):\n",
    "                        break\n",
    "                    myfile2.write(f'{column}\\n' )"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
