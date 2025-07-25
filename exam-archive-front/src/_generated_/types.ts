export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
export type MakeEmpty<T extends { [key: string]: unknown }, K extends keyof T> = { [_ in K]?: never };
export type Incremental<T> = T | { [P in keyof T]?: P extends ' $fragmentName' | '__typename' ? T[P] : never };
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: { input: string; output: string; }
  String: { input: string; output: string; }
  Boolean: { input: boolean; output: boolean; }
  Int: { input: number; output: number; }
  Float: { input: number; output: number; }
  Date: { input: any; output: any; }
  DateTime: { input: any; output: any; }
  GenericScalar: { input: any; output: any; }
  JSONString: { input: any; output: any; }
  Upload: { input: any; output: any; }
};

export type DifficultyRatingType = {
  __typename?: 'DifficultyRatingType';
  difficultyScore: FetenaarchiveDifficultyRatingDifficultyScoreChoices;
  exam: ExamType;
  id: Scalars['ID']['output'];
  ratedAt: Scalars['DateTime']['output'];
  ratedBy: UserType;
};

export type ExamFileType = {
  __typename?: 'ExamFileType';
  exam: ExamType;
  file: Scalars['String']['output'];
  id: Scalars['ID']['output'];
};

export type ExamType = {
  __typename?: 'ExamType';
  course: Scalars['String']['output'];
  department: Scalars['JSONString']['output'];
  difficultyratingSet: Array<DifficultyRatingType>;
  examFile: Array<ExamFileType>;
  id: Scalars['ID']['output'];
  peerreviewSet: Array<PeerReviewType>;
  title: FetenaarchiveExamTitleChoices;
  uploadDate: Scalars['Date']['output'];
  uploadedBy: UserType;
  visibility: FetenaarchiveExamVisibilityChoices;
  year: Scalars['Int']['output'];
};

/** An enumeration. */
export enum FetenaarchiveDifficultyRatingDifficultyScoreChoices {
  /** VERY EASY */
  A_1 = 'A_1',
  /** EASY */
  A_2 = 'A_2',
  /** MODERATE */
  A_3 = 'A_3',
  /** HARD */
  A_4 = 'A_4',
  /** VERY HARD */
  A_5 = 'A_5'
}

/** An enumeration. */
export enum FetenaarchiveExamTitleChoices {
  /** Final */
  Final = 'FINAL',
  /** Mid */
  Mid = 'MID',
  /** Quiz */
  Quiz = 'QUIZ'
}

/** An enumeration. */
export enum FetenaarchiveExamVisibilityChoices {
  /** Archived */
  Archived = 'ARCHIVED',
  /** Draft */
  Draft = 'DRAFT',
  /** Published */
  Published = 'PUBLISHED'
}

/** An enumeration. */
export enum FetenaarchiveUserRoleChoices {
  /** Lecturer */
  Lecturer = 'LECTURER',
  /** Staff */
  Staff = 'STAFF',
  /** Student */
  Student = 'STUDENT'
}

export type Mutation = {
  __typename?: 'Mutation';
  createUser?: Maybe<CreateUser>;
  refreshToken?: Maybe<Refresh>;
  /** Obtain JSON Web Token mutation */
  tokenAuth?: Maybe<ObtainJsonWebToken>;
  uploadFile?: Maybe<UploadExamMutation>;
  verifyToken?: Maybe<Verify>;
};


export type MutationCreateUserArgs = {
  email: Scalars['String']['input'];
  password: Scalars['String']['input'];
  role: Scalars['String']['input'];
  staffID?: InputMaybe<Scalars['String']['input']>;
  studentID?: InputMaybe<Scalars['String']['input']>;
  username: Scalars['String']['input'];
};


export type MutationRefreshTokenArgs = {
  token?: InputMaybe<Scalars['String']['input']>;
};


export type MutationTokenAuthArgs = {
  password: Scalars['String']['input'];
  username: Scalars['String']['input'];
};


export type MutationUploadFileArgs = {
  file: Scalars['Upload']['input'];
};


export type MutationVerifyTokenArgs = {
  token?: InputMaybe<Scalars['String']['input']>;
};

/** Obtain JSON Web Token mutation */
export type ObtainJsonWebToken = {
  __typename?: 'ObtainJSONWebToken';
  payload: Scalars['GenericScalar']['output'];
  refreshExpiresIn: Scalars['Int']['output'];
  token: Scalars['String']['output'];
};

export type PeerReviewType = {
  __typename?: 'PeerReviewType';
  examID: ExamType;
  id: Scalars['ID']['output'];
  reviewText: Scalars['String']['output'];
  reviewedAt: Scalars['DateTime']['output'];
  reviewerID: UserType;
};

export type Query = {
  __typename?: 'Query';
  allExams?: Maybe<Array<Maybe<ExamType>>>;
  difficultyRating?: Maybe<Array<Maybe<DifficultyRatingType>>>;
  difficultyRatingByExam?: Maybe<Array<Maybe<DifficultyRatingType>>>;
  examByCourse?: Maybe<Array<Maybe<ExamType>>>;
  examByTitle?: Maybe<Array<Maybe<ExamType>>>;
  examByYear?: Maybe<ExamType>;
  files?: Maybe<Array<Maybe<ExamFileType>>>;
  peerReviewById?: Maybe<Array<Maybe<PeerReviewType>>>;
  userById?: Maybe<UserType>;
};


export type QueryDifficultyRatingByExamArgs = {
  examId: Scalars['Int']['input'];
};


export type QueryExamByCourseArgs = {
  course: Scalars['String']['input'];
};


export type QueryExamByTitleArgs = {
  title: Scalars['String']['input'];
};


export type QueryExamByYearArgs = {
  year: Scalars['Int']['input'];
};


export type QueryPeerReviewByIdArgs = {
  examId: Scalars['Int']['input'];
};


export type QueryUserByIdArgs = {
  id?: InputMaybe<Scalars['String']['input']>;
};

export type Refresh = {
  __typename?: 'Refresh';
  payload: Scalars['GenericScalar']['output'];
  refreshExpiresIn: Scalars['Int']['output'];
  token: Scalars['String']['output'];
};

export type UploadExamMutation = {
  __typename?: 'UploadExamMutation';
  success?: Maybe<Scalars['Boolean']['output']>;
};

export type UserType = {
  __typename?: 'UserType';
  email: Scalars['String']['output'];
  id: Scalars['ID']['output'];
  role: FetenaarchiveUserRoleChoices;
  staffID: Scalars['String']['output'];
  /** Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. */
  username: Scalars['String']['output'];
};

export type Verify = {
  __typename?: 'Verify';
  payload: Scalars['GenericScalar']['output'];
};

export type CreateUser = {
  __typename?: 'createUser';
  user?: Maybe<UserType>;
};
