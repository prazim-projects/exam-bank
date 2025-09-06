import {defineStore} from 'pinia'
import apolloClient from '~/plugins/apollo-client'
import piniaPersistedstate from '~/plugins/pinia-persistedstate'

export const useUserStore = defineStore('exam', ()=> {
    // type definition
    interface DifficultyRating {
        difficultyScore: string;
        id: string;
        ratedAt: string;
    }

    interface ExamFile {
        file: File;
        id: string;
    }

    interface PeerReview {
        id: string;
        reviewText: string;
        rating: number;
        reviewedAt: string;
    }

    interface Exam {
        email: string;
        id: string;
        role: string;
        studentID: string;
        username: string;
        year: number;
    }
    // State
    const exam = ref<Exam | null>(null);
    const examFiles = ref<ExamFile[]>([]);
    const difficultyRatings = ref<DifficultyRating[]>([]);
    const peerReviews = ref<PeerReview[]>([]);
})