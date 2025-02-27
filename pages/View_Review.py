import streamlit as st



# Logo
image = "assets/logo.png"
st.logo(image, size='large')

# Page Title
st.title("View Reviews📨")
st.write("Our Reviews")


# Declaring class
class QueueWithReverse:
    ARCHIVE_PATH = "review_records.txt"
    THRESHOLD = 9

    def __init__(self):
        """Initialize the queue with a fixed limit."""
        self.limit = self.THRESHOLD
        self.storage = []

    def enqueue(self, entry):
        """Add a new entry to the queue. If full, remove the oldest entry."""
        if self.is_full():
            self.dequeue()
        self.storage.append(entry)

    def dequeue(self):
        """Remove and return the oldest entry in the queue, if available."""
        if not self.is_empty():
            return self.storage.pop(0)
        return None

    def size(self):
        """Return the current number of entries in the queue."""
        return len(self.storage)

    def is_full(self):
        """Check if the queue has reached its limit."""
        return self.size() >= self.limit
    
    def is_empty(self):
        """Check if the queue is empty."""
        return self.size() == 0

    def retrieve(self, reversed_order=False):
        """Retrieve all entries in normal or reversed order."""
        return self.storage[::-1] if reversed_order else self.storage

def extract_reviews():
    """Retrieve archived review entries and load them into the queue."""
    repository = QueueWithReverse()
    try:
        with open(QueueWithReverse.ARCHIVE_PATH, "r", encoding="utf-8") as archive:
            for note in archive:
                repository.enqueue(note.strip())
    except FileNotFoundError:
        pass  # If file does not exist, start with an empty queue
    return repository


def preserve_reviews(repository):
    """Save the current queue entries back to the archive file."""
    with open(QueueWithReverse.ARCHIVE_PATH, "w", encoding="utf-8") as archive:
        for entry in repository.retrieve():
            archive.write(entry.replace("\n", " ") + "\n")



# Load existing reviews
rqueue = extract_reviews()
reviews = rqueue.retrieve()

# Display Recent reviews
st.header("Echoes of the Community")

if reviews:
    total_entries = len(reviews)
    for i in range(0, total_entries, 3):
        columns = st.columns(min(3, total_entries - i))
        for j in range(min(3, total_entries - i)):
            with columns[j]:
                st.write(f"✍️ {reviews[i + j]}")
else:
    st.write("No reviews yet. Be the first to leave your mark! ✨")

# Review Submission Section
st.subheader("Your Thoughts Matter 💬")
input_reflection = st.text_area("Pen down your reflections:").strip()

if st.button("Share Reflection"):
    if input_reflection:
        rqueue.enqueue(input_reflection)
        preserve_reviews(rqueue)
        st.balloons()
        st.success("Your reviews are cherished!")
        st.rerun()

        
    else:
        st.warning("An empty reflection? Surely, you must have something to share!")